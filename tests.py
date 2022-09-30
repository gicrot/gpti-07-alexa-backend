# standard
import json

# test
from unittest import TestCase

# utils
from utils import parse_bencina
from utils import parse_comuna

# lambda function
from lambda_function import lambda_handler

class TestsUtils(TestCase):
    def setUp(self):
        return super().setUp()

    def test_parse_comuna_with_accent(self):
        event_input = "San Joaquín"
        parsed_input = parse_comuna(event_input)
        self.assertEqual(parsed_input, "san joaquin")

    def test_parse_comuna_with_tt(self):
        event_input = "Puerto Montt"
        parsed_input = parse_comuna(event_input)
        self.assertEqual(parsed_input, "puerto montt")

    def test_parse_comuna_with_ñ(self):
        event_input = "Puerto Montt"
        parsed_input = parse_comuna(event_input)
        self.assertEqual(parsed_input, "puerto montt")

    def test_parse_existing_fuel(self):
        event_input = "95"
        parsed_input = parse_bencina(event_input)
        self.assertEqual(parsed_input, "95")

    def test_bad_parse_fuel(self):
        event_input = "99"
        parsed_input = parse_bencina(event_input)
        self.assertEqual(parsed_input, "Error")


class TestAPIStatus(TestCase):
    def setUp(self):
        self.event_input = { "queryStringParameters": {} }
        self.event_data= {
            "comuna": None,
            "bencina": None
        }
        return super().setUp()

    def test_200_status(self):
        self.event_data["comuna"] = "San joaquín"
        self.event_data["bencina"] = "95"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        self.assertEqual(response["statusCode"], 200)

    def test_bad_commune(self):
        self.event_data["comuna"] = "San xoaquín"
        self.event_data["bencina"] = "97"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        self.assertEqual(response["statusCode"], 400)

    def test_bad_fuel(self):
        self.event_data["comuna"] = "San joaquín"
        self.event_data["bencina"] = "99"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        self.assertEqual(response["statusCode"], 400)

    def test_commune_with_ñ(self):
        self.event_data["comuna"] = "Camiña"
        self.event_data["bencina"] = "diesel"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        self.assertEqual(response["statusCode"], 200)

    def test_commune_with_gas_instead_of_fuel(self):
        self.event_data["comuna"] = "Puerto Montt"
        self.event_data["bencina"] = "93"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        self.assertEqual(response["statusCode"], 200)


class TestAPIBody(TestCase):
    def setUp(self):
        self.event_input = { "queryStringParameters": {} }
        self.event_data= {
            "comuna": None,
            "bencina": None
        }
        return super().setUp()

    def test_max_three_events(self):
        self.event_data["comuna"] = "Maipú"
        self.event_data["bencina"] = "93"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        data = json.loads(response["body"])
        self.assertTrue(len(data) <= 3)

    def test_three_events(self):
        self.event_data["comuna"] = "Las Condes"
        self.event_data["bencina"] = "95"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        data = json.loads(response["body"])
        self.assertEqual(len(data), 3)

    def test_prices_in_order(self):
        self.event_data["comuna"] = "La Florida"
        self.event_data["bencina"] = "petroleo"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        data = json.loads(response["body"])
        prices = [
            dat["precio"]
            for dat in data
        ]
        self.assertTrue(prices[0] <= prices[1] <= prices[2])

    def test_api_with_400(self):
        self.event_data["comuna"] = ""
        self.event_data["bencina"] = "99"
        self.event_input["queryStringParameters"] = self.event_data
        response = lambda_handler(self.event_input, {})
        data = json.loads(response["body"])
        self.assertNotIsInstance(data, list)
