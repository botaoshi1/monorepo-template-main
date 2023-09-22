import unittest
import jsonapi

class ExtendedEncoderTest(unittest.TestCase):
    def test_complex_encode1(self):
        my_data = {"real": 1.0, "imag": 2.0,}
        json_data = jsonapi.dumps(my_data)
        self.assertEqual(json_data, '{"real": 1.0, "imag": 2.0}')

    def test_complex_encode2(self):
        my_data = 1+2j
        json_data = jsonapi.dumps(my_data)
        self.assertEqual(json_data, '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}')

    def test_range_encode(self):
        my_data = range(1, 10, 3)
        json_data = jsonapi.dumps(my_data)
        self.assertEqual(json_data, '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}')

    def test_encode(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        json_data = jsonapi.dumps(my_data)
        self.assertEqual(json_data, '{"hey": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "there": {"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}, "73": false}')

class ExtendedDecoderTest(unittest.TestCase):
    def test_complex_decode1(self):
        json_data = '{"real": 1.0, "imag": 2.0}'
        my_data = jsonapi.loads(json_data)
        self.assertEqual(my_data, {"real": 1.0, "imag": 2.0})

    def test_complex_decode2(self):
        json_data = '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
        my_data = jsonapi.loads(json_data)
        self.assertEqual(my_data, 1+2j)

    def test_range_decode(self):
        json_data = '{"start": 1, "stop": 10, "step": 1, "__extended_json_type__": "range"}'
        my_data = jsonapi.loads(json_data)
        self.assertEqual(my_data, range(1, 10))

    def test_decode(self):
        json_data = '{"hey": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "there": {"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}, "73": false}'
        my_data = jsonapi.loads(json_data)
        self.assertEqual(my_data, {'hey': (1+2j), 'there': range(1, 10, 3), '73': False})

if __name__ == "__main__":
    unittest.main()
