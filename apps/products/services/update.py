from apps.products.models import Product, ProductPrice
from apps.products.amazon_scraper import scrape
from django.db import IntegrityError, transaction

class UpdateProductPrice:

    def execute(self):
        products = Product.objects.all()
        for product in products:
            try:
                try:
                    latest_product_price = product.productprice_set.latest('created_at')
                except ProductPrice.DoesNotExist:
                    latest_product_price = None
                scrape_obj = scrape(product.link)
                if latest_product_price is None:
                    self._save_product_price(price=scrape_obj['price'], product=product)
                else:
                    if str(latest_product_price.price) != str(scrape_obj['price']):
                        print("Masuk sini %s dan %s" % (str(latest_product_price.price), str(scrape_obj['price'])))
                        self._save_product_price(price=scrape_obj['price'], product=product)
            except Exception as error:
                print('Caught this error: ' + repr(error))
                # log to honeybadger or kibana
                pass

    def _save_product_price(self, **kwargs):
        try:
            with transaction.atomic():
                price = kwargs['price']
                product = kwargs['product']
                new_product_price = ProductPrice(price=price)
                new_product_price.product = product
                new_product_price.save()
        except IntegrityError as error:
            print('Caught this error: ' + repr(error))
            # log to honeybadger or kibana
            transaction.rollback()

class UpdateProduct:

    def execute(self):
        products = Product.objects.all()
        for product in products:
            try:
                scrape_obj = scrape(product.link)
                with transaction.atomic():
                    product.price = scrape_obj['price']
                    product.description = scrape_obj['name']
                    product.image_urls = scrape_obj['images']
                    product.save()
            except IntegrityError as error:
                print('Caught this error: ' + repr(error))
                # log to honeybadger or kibana
                transaction.rollback()