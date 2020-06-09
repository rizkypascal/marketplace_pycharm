from django.apps import AppConfig

class ProductsConfig(AppConfig):
    name = 'apps.products'

    def ready(self):
        from apps.products.scheduler import start
        start()
