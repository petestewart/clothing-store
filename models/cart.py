from flask_restful import Resource, fields, marshal_with


class CartItem(dict):
    """Model for Cart Item"""
    def __init__(self, item):
        dict.__init__(self, id=item['id'], name=item['name'], price=item['price'], quantity=1)

class Cart():
    """Model for Cart"""
    def __init__(self, tax_rate, shipping_rate):
        self.cart = []
        self.tax_rate = tax_rate
        self.shipping_rate = shipping_rate

    def totals_due(self):
        total_items = 0
        subtotal = 0
        for line in self.cart:
            total_items += line["quantity"]
            subtotal += (line["price"] * line["quantity"])
        tax = round((subtotal * (self.tax_rate / 100)), 2)
        final_total = subtotal + tax + self.shipping_rate
        return {
            'total_items': total_items,
            'subtotal': subtotal,
            'tax': tax,
            'shipping': self.shipping_rate,
            'final_total': final_total
        }


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

    def remove(self, item_id, amount):
        for existing_item in self.cart:
            # check if item is in cart
            if existing_item['id'] == item_id:
                # if the amount to remove is at least as much as the current quantity or no amount is given, remove the item completely
                if amount is None or amount >= existing_item['quantity']:
                    self.cart.remove(existing_item)
                    return self.cart
                # if the amount to remove is less than the current quantity, reduce the quantity appropriately
                if amount > 0 and amount < existing_item['quantity']:
                    existing_item['quantity'] -= amount
                    return self.cart

    def objects(self):
        view_cart = {
            'items': [],
            'totals_due': {}
        }
        for line in self.cart:
            line["line_total"] = line["price"] * line["quantity"]
            view_cart["items"].append(line)
        view_cart["totals_due"] = self.totals_due()
        return view_cart