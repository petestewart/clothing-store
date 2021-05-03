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

    def test_get_catalog(self):
        """Ensure that API retrieves the catalog"""
        res = self.client().get('/catalogitems')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), len(CATALOG_ITEMS))
        self.assertEqual(data, CATALOG_ITEMS)


if __name__ == '__main__':
    unittest.main()
