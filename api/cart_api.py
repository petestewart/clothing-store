from flask_restful import Resource, reqparse

from services import cart_service



parser = reqparse.RequestParser()

class CartApi(Resource):
    """Resource for Cart"""

    def get(self):
        """Get response method for returning cart"""
        return cart_service.get_all_cart_items_and_totals()

    def post(self):
        """Add item to cart"""
        # parse item_id and quantity from request body
        parser.add_argument('item_id', type=str)
        parser.add_argument('quantity', type=int)
        args = parser.parse_args()
        return cart_service.add_item_to_cart(args)

    def patch(self):
        """Remove item(s) from cart"""
        # parse item_id and quantity from request body
        parser.add_argument('item_id', type=str)
        parser.add_argument('quantity', type=int)
        args = parser.parse_args()
        return cart_service.remove_items_from_cart(args)

    def delete(self):
        """Clear all items from cart"""
        return cart_service.clear_cart()