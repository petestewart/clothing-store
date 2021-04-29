import unittest
from api import catalogitem

class CatalogTest(unittest.TestCase):
    def test_get_catalog(self):
        """Ensure a list is returned"""
        result = catalogitem.get()
        self.assertEqual(isinstance(result), result)

if __name__ == '__main__':
    unittest.main()
