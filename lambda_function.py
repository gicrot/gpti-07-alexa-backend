# standard
import json
import os
import requests
import secret

# comunas
from comunas import region_por_comuna

# utils
from utils import get_top_three_fuel_prices
from utils import normalize
from utils import parse_bencina
from utils import parse_comuna


CNE_URL = secret.CNE_URL
TOKEN = secret.CNE_TOKEN
if os.environ.get("CNE_URL"):
    CNE_URL = os.environ.get("CNE_URL")
    TOKEN = os.environ.get("CNE_TOKEN")

def get_comuna_id(comuna):
    """
    Function that gets the id in CNE api
    to be used in the request
    """
    try:
        response = requests.get(
            f"{CNE_URL}/comunas",
            params={
                "token": TOKEN,
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

def get_fuel_prices_in_comuna(comuna, comuna_id, bencina):
    """
    Function that gets the fuel prices from
    the CNE API
    """
    response = requests.get(
        f"{CNE_URL}/combustibles/vehicular/estaciones",
        params={
            "token": TOKEN,
            "region": [region_por_comuna[comuna]],
            "comuna": [comuna_id],
        }
    )

    bencina_parser = {
        "93": "gasolina 93",
        "95": "gasolina 95",
        "97": "gasolina 97",
        "diesel": "petroleo diesel",
        "petroleo": "petroleo diesel",
    }

    data = [
        {
            "distribuidor": price_data["distribuidor"]["nombre"],
            "direccion": f"{price_data['direccion_calle']} {price_data['direccion_numero']}",
            "bencina": bencina_parser[bencina],
            "precio": price_data["precios"][bencina_parser[bencina]],
        }
        for price_data in response.json()["data"]
    ]

    return data

# GET -> params: comuna, bencina
def lambda_handler(event, context):
    """
    Handler that is executed by lambda function
    """
    event_input = event["queryStringParameters"]
    comuna = parse_comuna(event_input.get("comuna", ""))
    comuna_id = get_comuna_id(comuna)

    if comuna_id == "Error":
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Comuna <{comuna}> no encontrada"})
        }
    raw_bencina = event_input.get("bencina", "")
    bencina = parse_bencina(raw_bencina)
    if bencina == "Error":
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Tipo de bencina <{raw_bencina}> no encontrada"})
        }
    fuel_prices = get_fuel_prices_in_comuna(comuna, comuna_id, bencina)

    top_three = get_top_three_fuel_prices(fuel_prices)

    return {
        'statusCode': 200,
        'body': json.dumps(top_three)
    }

if __name__ == "__main__":
    event = {
        "queryStringParameters": {
            "comuna": "San Joaquín",
            "bencina": "95"
        }
    }
    wrong_comune = {
        "queryStringParameters": {
            "comuna": "Comuna mala",
            "bencina": "95"
        }
    }
    wrong_fuel = {
        "queryStringParameters": {
            "comuna": "San Joaquín",
            "bencina": "1000"
        }
    }
    context = {}
    print(f"CASO CORRECTO: {lambda_handler(event, context)}\n")
    print(f"CASO COMUNA ERRONEA: {lambda_handler(wrong_comune, context)}\n")
    print(f"CASO BENCINA ERRONEA: {lambda_handler(wrong_fuel, context)}\n")
