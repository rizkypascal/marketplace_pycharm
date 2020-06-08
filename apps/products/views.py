from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from apps.products.serializers.product_serializer import ProductSerializer
from apps.products.services.create import CreateProduct
import json
# Create your views here.

def index(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return render(request, 'product_list.html',
                  {'data': serializers.data})

def create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        link = form.cleaned_data['link']
        result = CreateProduct(link=link).execute()
        if result is not None:
            return HttpResponseRedirect('/products/' + str(result.id) + '/')
        else:
            messages.error(request, "Product Insertion Failed")
    return render(request, 'product_form.html', {'form': form})

def form(request):
    form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def detail(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return render(request, 'product_detail.html',
                  {'data': serializer.data})