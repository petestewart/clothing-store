from flask_restful import Api

from api.catalogitem import CatalogItemsApi
from api.cart import CartApi

def create_routes(api: Api):
    """Adds resources to api and attaches routes"""
    
    api.add_resource(CatalogItemsApi, '/catalogitems')
    api.add_resource(CartApi, '/cart')