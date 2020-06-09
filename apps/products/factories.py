import factory
from datetime import datetime
from . import models
import json

class ProductFactory(factory.Factory):
    class Meta:
        model = models.Product

    id = 1
    link = 'https://www.amazon.com'
    price = '$5.00'
    description = 'Product A'
    image_urls = json.dumps(['a'])

class ProductPriceFactory(factory.Factory):
    class Meta:
        model = models.ProductPrice

    id = 1
    price = '$10.00'
    created_at = datetime.now()
    product = factory.SubFactory(ProductFactory)