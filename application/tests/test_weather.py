import unittest
from models.weather import get_weather

class TestWeather(unittest.TestCase):
    def test_get_weather(self):
        # Test case 1: Add your test case here
        result = get_weather("Nairobi", "C")
        self.assertIn("Nairobi", result)

        # Test case 2: Add another test case if needed
        result = get_weather("New York", "F")
        self.assertIn("New York", result)

if __name__ == '__main__':
    unittest.main()
