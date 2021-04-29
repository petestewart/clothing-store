from flask_restful import Resource, reqparse

from models.cart import Cart
from database.catalogitems import CATALOG_ITEMS

user_cart = Cart(8.9, 4)
parser = reqparse.RequestParser()

class CartApi(Resource):
    """Resource for Cart"""

    def get(self):
        """Get response method for returning cart"""
        return user_cart.objects()

    def post(self):
        """Add item to cart"""
        # parse item_id from request body
        parser.add_argument('item_id', type=str)
        args = parser.parse_args()

        # check if item is in catalog
        new_item = None
        for available_item in CATALOG_ITEMS:
            if available_item['id'] == args['item_id']:
                new_item = available_item
        if new_item is None:
            return 'Item not available', 404

        # add new_item to cart
        user_cart.add(new_item)
        return user_cart.objects(), 201

    def delete(self):
        """Remove item(s) from cart"""
        # parse item_id and amount from request body
        parser.add_argument('item_id', type=str)
        parser.add_argument('amount', type=int)
        args = parser.parse_args()

        # checks if item is in cart
        cart_item_ids = [item['id'] for item in user_cart.objects()]
        if args['item_id'] in cart_item_ids:
            # item is in cart, call the cart's remove method
            result = user_cart.remove(args['item_id'], args['amount'])
            return result, 200

        # otherwise let the user know nothing has been deleted
        return 'Item not in cart', 400