from flask_restful import Resource, fields, marshal_with

from database.catalogitems import CATALOG_ITEMS

# resource_fields = {
#     'name': fields.String,
#     'price': fields.String,
#     'id': fields.String
# }

# class CatalogItems():
#     """Model for Catalog Items"""
#     @marshal_with(resource_fields)
#     def friendly_view(self):
#         return CATALOG_ITEMS

class CatalogItems(dict):
    """Model for Catalog Item"""
    def __init__(self, item):
        dict.__init__(self, id=item['id'], name=item['name'], price=item['price'])