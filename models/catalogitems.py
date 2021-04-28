from flask_restful import Resource, fields, marshal_with

from database.catalogitems import CATALOG_ITEMS

resource_fields = {
    'name': fields.String,
    'price': fields.Float,
}

# class CatalogItems(Resource):
#     @marshal_with(resource_fields, envelope='resource')


class CatalogItems(Resource):
    @marshal_with(resource_fields)
    def objects(self):
        return CATALOG_ITEMS