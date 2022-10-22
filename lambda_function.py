# standard
import json
import os
import secret

# api
from api import api

CNE_URL = None
TOKEN = None

# GET -> params: comuna, bencina
def lambda_handler(event, context):
    """
    Handler that is executed by lambda function
    """
    event_input = event.get("queryStringParameters", None)
    if not event_input:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Not found query params"})
        }

    CNE_URL = os.environ.get("CNE_URL", secret.CNE_URL)
    TOKEN = os.environ.get("CNE_TOKEN", secret.CNE_TOKEN)

    return api(event, CNE_URL, TOKEN)

if __name__ == "__main__":
    event = {
        "queryStringParameters": {
            "comuna": "San Joaquín",
            "bencina": "95"
        }
    }
    event_two_communes = {
        "queryStringParameters": {
            "comuna": "San Joaquín",
            "comuna2": "Macul",
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
    print(f"CASO CORRECTO MULTIPLES COMUNAS: {lambda_handler(event_two_communes, context)}\n")
    print(f"CASO COMUNA ERRONEA: {lambda_handler(wrong_comune, context)}\n")
    print(f"CASO BENCINA ERRONEA: {lambda_handler(wrong_fuel, context)}\n")
