import unittest
from pysenticrypt import SentiCryptAPI

class TestSentiCryptAPI(unittest.TestCase):

    def setUp(self):
        self.api = SentiCryptAPI()

    def test_get_all_data(self):
        data = self.api.get_all_data()
        self.assertIsInstance(data, list)

    def test_get_pretty_all_data(self):
        data = self.api.get_pretty_all_data()
        self.assertIsInstance(data, list)

    def test_get_index(self):
        data = self.api.get_index()
        self.assertIsInstance(data, list)

    def test_get_data_by_date(self):
        data = self.api.get_data_by_date("2023-04-17")
        self.assertIsInstance(data, dict)

if __name__ == "__main__":
    unittest.main()
