from rest_framework import serializers
from apps.products.models import Product, ProductPrice
from .product_price_serializer import ProductPriceSerializer
import json

class ProductSerializer(serializers.ModelSerializer):
    product_prices = ProductPriceSerializer(source='productprice_set', many=True)
    image_urls = serializers.SerializerMethodField()

    def get_image_urls(self, obj):
        return json.loads(obj.image_urls)

    class Meta:
        model = Product
        fields = ('id', 'link', 'description', 'price', 'image_urls', 'product_prices')