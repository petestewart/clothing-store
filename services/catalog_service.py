from models.catalogitems_model import CatalogItems
from database.catalogitems import CATALOG_ITEMS

catalog = CATALOG_ITEMS

def get_all_catalog_items():
    return catalog, 200