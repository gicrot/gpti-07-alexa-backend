import json
import os
import requests
import secret
from comunas import region_por_comuna
from utils import normalize


CNE_URL = secret.CNE_URL
TOKEN = secret.CNE_TOKEN
if os.environ.get("CNE_URL"):
    CNE_URL = os.environ.get("CNE_URL")
    TOKEN = os.environ.get("CNE_TOKEN")

def parse_input(event_input):
    """
    Function for parsing the input
    inside event
    """
    return normalize(event_input.lower())

def get_comuna_id(comuna):
    """
    Function that gets the id in CNE api
    to be used in the request
    """
    response = requests.get(
        f"{CNE_URL}/comunas",
        params={
            "token": TOKEN,
            "region": region_por_comuna[comuna]
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

def lambda_handler(event: dict["comuna": str, "bencina": str], context):
    """
    Handler that is executed by lambda function
    """
    comuna = parse_input(event["comuna"])
    comuna_id = get_comuna_id(comuna)
    print(comuna_id)

    return {
        'statusCode': 200,
        'body': json.dumps({"message": 'Hello from Lambda!', "token": TOKEN})
    }

if __name__ == "__main__":
    event = { "comuna": "San Joaquín", "bencina": 95 }
    context = {}
    print(lambda_handler(event, context))