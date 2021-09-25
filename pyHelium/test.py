import unittest
# api = __import__("../api")
from api import Api

class TestApi(unittest.TestCase):


    def test_get_hotpost_data_from_address(self):
        self.api = Api()
        response = self.api.get_hotpost_data_from_address("112QSpGNhHgZh5bXZuEFLwnKvfGf9N6ujErf7A97xkgi81HQogAX")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
