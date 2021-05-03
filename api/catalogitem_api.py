from flask_restful import Resource

from services import catalog_service

# from models.catalogitems_model import CatalogItems


class CatalogItemsApi(Resource):
    """Resource for returning CatalogItems collection"""

    def get(self):
        """GET response method for all items in catalog"""
        return catalog_service.get_all_catalog_items()