from flask_restful import Api

from api.catalogitem_api import CatalogItemsApi
from api.cart_api import CartApi

def create_routes(api: Api):
    """Adds resources to api and attaches routes"""
    
    api.add_resource(CatalogItemsApi, '/catalogitems')
    api.add_resource(CartApi, '/cart')
    # api.add_resource(CartClearApi, '/cart/clear')