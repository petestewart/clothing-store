import unittest
import json
from app import app
from database.catalogitems import CATALOG_ITEMS

class CatalogTestCase(unittest.TestCase):
    """Catalog test case"""

    def setUp(self):
        """Initialize app"""
        self.app = app
        self.client = self.app.test_client

    
    def test_get_cart(self):
        """Ensure that API retrieves the catalog"""
        res = self.client().get('/cart')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['items'], list)
        self.assertEqual(len(data['items']), 0)

if __name__ == '__main__':
    unittest.main()