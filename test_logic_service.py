import unittest
from logic_service import calculate_response

class test_logic_service(unittest.TestCase):

    def test_empty_dict(self):
        data = {}
        self.assertEqual(calculate_response(data), "Input is invalid")
    
    def test_missing_input(self):
        data = {
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "on"
        }
        self.assertEqual(calculate_response(data), "Input is invalid")

    def test_excess_input(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "on",
            "light_indicator3" : "off",
            "light_indicator4" : "off"
        }
        self.assertEqual(calculate_response(data), "Input is invalid")

    def test_serial_number_24(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "on",
            "light_indicator3" : "off"
        }
        self.assertEqual(calculate_response(data), "Please upgrade your device")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "34-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "on",
            "light_indicator3" : "off"
        }
        self.assertNotEqual(calculate_response(data), "Please upgrade your device")

    def test_serial_number_36(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "36-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "off",
            "light_indicator3" : "off"
        }
        self.assertEqual(calculate_response(data), "Turn on the device")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "36-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "ALL is ok")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "36-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "blinking",
            "light_indicator3" : "blinking"
        }
        self.assertEqual(calculate_response(data), "Please wait")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "36-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "off",
            "light_indicator3" : "blinking"
        }
        self.assertEqual(calculate_response(data), "Cannot assist at this moment")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "36-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "blinking",
            "light_indicator2" : "blinking",
            "light_indicator3" : "blinking"
        }
        self.assertEqual(calculate_response(data), "Cannot assist at this moment")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "34-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertNotEqual(calculate_response(data), "Turn on the device")
        self.assertNotEqual(calculate_response(data), "Please wait")
        self.assertNotEqual(calculate_response(data), "ALL is ok")

    def test_serial_number_51(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "off",
            "light_indicator2" : "off",
            "light_indicator3" : "off"
        }
        self.assertEqual(calculate_response(data), "Turn on the device")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "off",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "ALL is ok")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "off",
            "light_indicator3" : "off"
        }
        self.assertEqual(calculate_response(data), "Cannot assist at this moment")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "blinking",
            "light_indicator3" : "off"
        }
        self.assertEqual(calculate_response(data), "Please wait")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "blinking",
            "light_indicator2" : "blinking",
            "light_indicator3" : "blinking"
        }
        self.assertEqual(calculate_response(data), "Please wait")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "51-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "off",
            "light_indicator3" : "on"
        }
        self.assertNotEqual(calculate_response(data), "Turn on the device")
        self.assertNotEqual(calculate_response(data), "Please wait")
        self.assertNotEqual(calculate_response(data), "ALL is ok")

    def test_serial_number_is_number(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : 1234567890123456789012345678901234567890123456789012345678901234,
            "light_indicator1" : "on",
            "light_indicator2" : "off",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "Bad serial number")

    def test_serial_number_not_24_36_51(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "17-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "Unknown device")

    def test_too_long_problem_description(self):
        data = {
            "problem_description" : "ProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblameticProblametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "Cannot accept problem description longer than 300 characters")

        data = {
            "problem_description" : "Problametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertNotEqual(calculate_response(data), "Cannot accept problem description longer than 300 characters")

    def test_serial_number_length(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "on",
            "light_indicator2" : "on",
            "light_indicator3" : "on"
        }
        self.assertEqual(calculate_response(data), "Serial number should consist of 64 characters exactly, please check")

    def test_wrong_light_status(self):
        data = {
            "problem_description" : "Problametic",
            "serial_number" : "24-X-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
            "light_indicator1" : "onn",
            "light_indicator2" : "on",
            "light_indicator3" : "blink"
        }
        self.assertEqual(calculate_response(data), "The status of light 1 and light 3 is invalid")


if __name__ == '__main__':
    unittest.main()