# standard
import json
import os
import requests

# comunas
from comunas import region_por_comuna

# utils
from utils import get_top_three_fuel_prices
from utils import normalize
from utils import parse_bencina
from utils import parse_comuna

def get_comuna_id(comuna, cne_url, token):
    """
    Function that gets the id in CNE api
    to be used in the request
    """
    try:
        response = requests.get(
            f"{cne_url}/comunas",
            params={
                "token": token,
                "region": region_por_comuna[comuna],
            }
        )
        
        data = [
            {
                "cod_comuna": comuna["cod_comuna"],
                "nom_comuna": normalize(comuna["nom_comuna"].lower())
            }
            for comuna in response.json()["data"]
        ]

        data_comuna = next(item for item in data if item["nom_comuna"] == comuna)

        return data_comuna["cod_comuna"]
    except KeyError:
        return "Error"

def get_fuel_prices_in_comuna(comunas_id, bencina, cne_url, token):
    """
    Function that gets the fuel prices from
    the CNE API
    """
    response = requests.get(
        f"{cne_url}/combustibles/vehicular/estaciones",
        params={
            "token": token,
            "comuna": [comunas_id],
        }
    )

    bencina_parser = {
        "93": "gasolina 93",
        "95": "gasolina 95",
        "97": "gasolina 97",
        "diesel": "petroleo diesel",
        "petroleo": "petroleo diesel",
    }

    parsed_bencina = bencina_parser.get(bencina, None)

    data = [
        {
            "distribuidor": price_data["distribuidor"]["nombre"],
            "direccion": f"{price_data['direccion_calle']} {price_data['direccion_numero']}",
            "bencina": parsed_bencina,
            "precio": price_data["precios"].get(parsed_bencina, 9999),
        }
        for price_data in response.json()["data"]
    ]

    return data

def api(event, cne_url, token):
    event_input = event.get("queryStringParameters", {})

    raw_comunas = []
    if event_input.get("comuna", False):
        raw_comunas.append(event_input["comuna"])
    if event_input.get("comuna2", False):
        raw_comunas.append(event_input["comuna2"])

    if len(raw_comunas) == 0:
        return {
                "statusCode": 400,
                "body": json.dumps({"error": f"Indica al menos una comuna"})
            }

    parsed_comunas = []
    for raw_comuna in raw_comunas:
        parsed_comunas.append(parse_comuna(raw_comuna))

    comunas_id = []
    for parsed_comuna in parsed_comunas:
        comuna_id = get_comuna_id(parsed_comuna, cne_url, token)
        if comuna_id == "Error":
            return {
                "statusCode": 400,
                "body": json.dumps({"error": f"Comuna <{parsed_comuna}> no encontrada"})
            }
        comunas_id.append(get_comuna_id(parsed_comuna, cne_url, token))

    raw_bencina = event_input.get("bencina", "")
    bencina = parse_bencina(raw_bencina)
    if bencina == "Error":
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Tipo de bencina <{raw_bencina}> no encontrada"})
        }
    fuel_prices = get_fuel_prices_in_comuna(comunas_id, bencina, cne_url, token)

    top_three = get_top_three_fuel_prices(fuel_prices)

    return {
        'statusCode': 200,
        'body': json.dumps(top_three)
    }
