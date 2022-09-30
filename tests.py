# test
from unittest import TestCase

# utils
from utils import parse_bencina
from utils import parse_comuna

class TestsUtils(TestCase):
    def setUp(self):
        return super().setUp()

    def test_parse_comuna_1(self):
        event_input = "San Joaquín"
        parsed_input = parse_comuna(event_input)
        self.assertEqual(parsed_input, "san joaquin")

    def test_parse_comuna_2(self):
        event_input = "Puerto Montt"
        parsed_input = parse_comuna(event_input)
        self.assertEqual(parsed_input, "puerto montt")

    def test_parse_bencina_1(self):
        event_input = "95"
        parsed_input = parse_bencina(event_input)
        self.assertEqual(parsed_input, "95")

    def test_bad_parse_bencina(self):
        event_input = "99"
        parsed_input = parse_bencina(event_input)
        self.assertIsNone(parsed_input)


class TestAPI(TestCase):
    def setUp(self):
        return super().setUp()
