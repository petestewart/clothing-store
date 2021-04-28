from flask_restful import Resource, fields, marshal_with

from database.catalogitems import CATALOG_ITEMS


class CartItem(dict):
    """Model for Cart Item"""
    def __init__(self, item):
        dict.__init__(self, id=item['id'], name=item['name'], price=item['price'], quantity=1)

class Cart(Resource):
    """Model for Cart"""
    def __init__(self):
        self.cart = []

    def add(self, item):
        # create new CartItem object from the item passed into method
        new_item = CartItem(item)

        # check if item is in cart and add to quantity if so
        for existing_item in self.cart:
            if existing_item['id'] == new_item['id']:
                existing_item['quantity'] += 1
                return self.cart 
        
        # otherwise, append the new item to the cart
        self.cart.append(new_item)
        return self.cart

    def objects(self):
        return self.cart