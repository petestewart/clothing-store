class CartItem(dict):
    """Model for Cart Item"""
    def __init__(self, item):
        dict.__init__(self, id=item['id'], name=item['name'], price=item['price'], quantity=1)