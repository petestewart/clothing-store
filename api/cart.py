from flask_restful import Resource, reqparse

from models.cart import Cart
from database.catalogitems import CATALOG_ITEMS

user_cart = Cart()
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