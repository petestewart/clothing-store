
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
        shipping_total = 0
        if subtotal > 0:
            shipping_total = self.shipping_rate
        final_total = subtotal + tax + shipping_total
        return {
            'total_items': total_items,
            'subtotal': subtotal,
            'tax': tax,
            'shipping': shipping_total,
            'final_total': final_total
        }

    def items_and_totals(self):
        view_cart = {
            'items': [],
            'totals_due': {}
        }
        for line in self.cart:
            line["line_total"] = line["price"] * line["quantity"]
            view_cart["items"].append(line)
        view_cart["totals_due"] = self.totals_due()
        return view_cart