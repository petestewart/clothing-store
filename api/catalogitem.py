from flask_restful import Resource

from models.catalogitems import CatalogItems


class CatalogItemsApi(Resource):
    """Resource for returning CatalogItems collection"""

    def get(self):
        """GET response method for all items in catalog"""
        
        catalog_items = CatalogItems()
        output = catalog_items.objects()
        return output, 200