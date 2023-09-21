import unittest
import jsonapi

class ExtendedEncoderTest(unittest.TestCase):
    def test_complex_encode(self):
        data = complex(5.0, 8.0)
        encoded_data = jsonapi.dumps(data)
        self.assertEqual(encoded_data, '{"__complex__": true, "real": 5.0, "imag": 8.0}')

    def test_range_encode(self):
        data = range(100, 200, 10)
        encoded_data = jsonapi.dumps(data)
        self.assertEqual(encoded_data, '{"__range__": true, "start": 100, "stop": 200, "step": 10}')

class ExtendedDecoderTest(unittest.TestCase):
    def test_complex_decode(self):
        json_data = '{"__complex__": true, "real": 5.0, "imag": 8.0}'
        decoded_data = jsonapi.loads(json_data)
        self.assertEqual(decoded_data, complex(5.0, 8.0))

    def test_range_decode(self):
        json_data = '{"__range__": true, "start": 100, "stop": 200, "step": 10}'
        decoded_data = jsonapi.loads(json_data)
        self.assertEqual(decoded_data, range(100, 200, 10))

if __name__ == "__main__":
    unittest.main()
