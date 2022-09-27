from unittest import TestCase
import lambda_function

class Tests(TestCase):
    def setUp(self):
        return super().setUp()

    def test_parse_input(self):
        event_input = "San Joaquín"
        parsed_input = lambda_function.parse_input(event_input)
        self.assertEqual(parsed_input, "san joaquin")
