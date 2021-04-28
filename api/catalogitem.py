from flask import Response, request, jsonify
from flask_restful import Resource

from models.catalogitems import CatalogItems


class CatalogItemsApi(Resource):
    """Resource for returning CatalogItems collection"""

    def get(self):
        """Get response method for all items in catalog"""

        catalog_items = CatalogItems()
        output = catalog_items.objects()
        return jsonify(output)