from models.cart_model import Cart
from models.cart_item_model import CartItem
from database.catalogitems import CATALOG_ITEMS


user_cart = Cart(8.9, 4)


def add_item_to_cart(args):
    # check if item is in catalog
    new_item = None
    for available_item in CATALOG_ITEMS:
        if available_item['id'] == args['item_id']:
            new_item = available_item
    if new_item is None:
        return 'Item not available', 404

    # set the quantity to the quantity in the request (or 1 if no quantity was supplied)
    quantity = 1
    if args['quantity'] is not None:
        quantity = args['quantity']

    new_item = CartItem(new_item)

    # add new_item to cart
    # check if item is in cart and add to quantity if so
    for existing_item in user_cart.cart:
        if existing_item['id'] == new_item['id']:
            existing_item['quantity'] += quantity
            existing_item['line_total'] = existing_item['quantity'] * existing_item['price']
            return user_cart.cart, 201

    # otherwise create new cart item and add to cart
    new_item['quantity'] = quantity
    new_item['line_total'] = new_item['quantity'] * new_item['price']
    user_cart.cart.append(new_item)

    return user_cart.cart, 201


def remove_items_from_cart(args):
    # checks if item is in cart
    cart_item_ids = [item['id'] for item in user_cart.cart]
    if args['item_id'] in cart_item_ids:
        # item is in cart, call the cart's remove method
        for existing_item in user_cart.cart:
            # check if item is in cart
            if existing_item['id'] == args['item_id']:
                # if the quantity to remove is at least as much as the current quantity or no quantity is given, remove the item completely
                if args['quantity'] is None or args['quantity'] >= existing_item['quantity']:
                    user_cart.cart.remove(existing_item)
                    return user_cart.cart, 200
                # if the quantity to remove is less than the current quantity, reduce the quantity appropriately
                if args['quantity'] > 0 and args['quantity'] < existing_item['quantity']:
                    existing_item['quantity'] -= args['quantity']
                    return user_cart.cart, 200
    # otherwise let the user know nothing has been deleted
    return 'Item not in cart', 400


def get_all_cart_items_and_totals():
    return user_cart.items_and_totals(), 200


def clear_cart():
    user_cart.cart = []
    return user_cart.cart, 200
