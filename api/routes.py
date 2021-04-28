from flask_restful import Api

from api.catalogitem import CatalogItemsApi

def create_routes(api: Api):
    """Adds resources to api and attaches routes"""

    api.add_resource(CatalogItemsApi, '/catalogitems')