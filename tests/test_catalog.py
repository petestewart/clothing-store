import unittest

from services import catalog_service
from database.catalogitems import CATALOG_ITEMS

class CatalogTestCase(unittest.TestCase):
    """Catalog test case"""

    def test_when_get_catalog_called_list_is_returned(self):
        res = catalog_service.get_all_catalog_items()
        self.assertIsInstance(res[0], list)
        self.assertEqual(res[1], 200)

    def test_when_get_catalog_called_list_matches_catalog_in_database(self):
        res = catalog_service.get_all_catalog_items()
        self.assertEqual(res[0], CATALOG_ITEMS)
        self.assertEqual(res[1], 200)

if __name__ == '__main__':
    unittest.main()
