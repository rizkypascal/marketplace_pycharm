from apps.products.models import Product
from apps.products.amazon_scraper import scrape
import json

class CreateProduct:

    def __init__(self, link):
        self._link = link

    def execute(self):
        try:
            scrape_obj = scrape(self._link)
            product = Product(
                link=self._link,
                price=scrape_obj['price'],
                description=scrape_obj['name'],
                image_urls=json.dumps(scrape_obj['images'])
            )
            product.save()
            return product
        except Exception as error:
            print('Caught this error: ' + repr(error))
            # log to honeybadger or kibana
            return None
