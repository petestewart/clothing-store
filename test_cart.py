import unittest

from services import cart_service, catalog_service

class CartTestCase(unittest.TestCase):
    """Catalog test case"""

    def setUp(self):
        cart_service.clear_cart()
        self.catalog = catalog_service.get_all_catalog_items()[0]

    def test_when_initial_get_cart_called_empty_list_is_returned(self):
        res = cart_service.get_all_cart_items_and_totals()
        self.assertIsInstance(res[0]['items'], list)
        self.assertEqual(len(res[0]['items']), 0)
        self.assertEqual(res[1], 200)

    def test_when_valid_item_is_added_to_cart_and_no_quantity_is_specified_cart_is_returned_with_item(self):
        item = self.catalog[0]
        res = cart_service.add_item_to_cart({'item_id': item['id'], 'quantity': None})
        cart = res[0]
        line = cart[0]
        self.assertEqual(len(cart), 1)
        self.assertEqual(line['id'], item['id'])
        self.assertEqual(line['quantity'], 1)

    def test_when_invalid_item_is_added_to_empty_cart_error_is_thrown(self):
        item_id = len(self.catalog) + 100
        assert item_id not in [item['id'] for item in self.catalog]
        res = cart_service.add_item_to_cart({'item_id': item_id, 'quantity': 1})
        self.assertEqual(res[1], 404)

    def test_when_valid_item_is_added_to_cart_cart_reflects_quantity_added(self):
        item = self.catalog[0]
        res = cart_service.add_item_to_cart({'item_id': item['id'], 'quantity': 5})
        cart = res[0]
        line = cart[0]
        self.assertEqual(len(cart), 1)
        self.assertEqual(line['id'], item['id'])
        self.assertEqual(line['quantity'], 5)

    def test_when_valid_second_item_is_added_to_cart_both_items_exist_in_cart(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        res = cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        cart = res[0]
        line1 = cart[0]
        line2 = cart[1]
        self.assertEqual(len(cart), 2)
        self.assertEqual(line1['id'], item1['id'])
        self.assertEqual(line1['quantity'], 5)
        self.assertEqual(line2['id'], item2['id'])
        self.assertEqual(line2['quantity'], 2)

    def test_when_item_is_removed_from_cart_with_no_quantity_specified_it_does_not_exist_in_cart(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart1 = cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})[0].copy()
        res = cart_service.remove_items_from_cart({'item_id': item1['id'], 'quantity': None})
        self.assertEqual(len(res[0]), 1)
        self.assertEqual(res[1], 200)
        self.assertNotEqual(cart1[0]['id'], item2['id'])

    def test_when_item_is_removed_by_quantity_the_cart_reflects_the_correct_quantity(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart1 = cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})[0].copy()
        res = cart_service.remove_items_from_cart({'item_id': item1['id'], 'quantity': 3})
        self.assertEqual(len(res[0]), len(cart1))
        self.assertEqual(res[1], 200)
        self.assertEqual(cart1[0]['quantity'], 2)

    def test_when_clear_cart_is_called_on_full_cart_an_empty_cart_is_returned(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        res = cart_service.clear_cart()
        self.assertEqual(len(res[0]), 0)

    def test_when_items_are_in_cart_the_total_items_are_correct(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        res = cart_service.user_cart.totals_due()
        self.assertEqual(res['total_items'], 7)

    def test_when_items_are_in_cart_the_subtotal_due_is_correct(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        expected_subtotal = (item1['price'] * 5) + (item2['price'] * 2)
        res = cart_service.user_cart.totals_due()
        self.assertEqual(res['subtotal'], expected_subtotal)

    def test_when_items_are_in_cart_the_final_total_due_is_correct(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart = cart_service.user_cart
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 5})
        cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        expected_total_due = ((((item1['price'] * 5) + (item2['price'] * 2)) * ((cart.tax_rate / 100) + 1)) + cart.shipping_rate)
        res = cart_service.user_cart.totals_due()
        self.assertEqual(res['final_total'], expected_total_due)

    def test_when_items_are_in_cart_the_line_totals_are_correct(self):
        item1 = self.catalog[0]
        item2 = self.catalog[1]
        cart = cart_service.user_cart
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 3})
        cart_service.add_item_to_cart({'item_id': item1['id'], 'quantity': 2})
        cart_service.add_item_to_cart({'item_id': item2['id'], 'quantity': 2})
        res = cart_service.get_all_cart_items_and_totals()[0]
        line_total1 = res['items'][0]['line_total']
        line_total2 = res['items'][1]['line_total']
        expected_line_total1 = item1['price'] * 5
        expected_line_total2 = item2['price'] * 2
        self.assertEqual(expected_line_total1, line_total1)
        self.assertEqual(expected_line_total2, line_total2)

if __name__ == '__main__':
    unittest.main()
