from rest_framework import serializers
from apps.products.models import ProductPrice

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('price', 'created_at')