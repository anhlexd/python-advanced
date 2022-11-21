from django.shortcuts import render
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from django.core.cache.backends.base import DEFAULT_TIMEOUT

# CACHE_TTL = getattr( settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
from .models import Product

@api_view(['GET'])

def get_products(request):
    print('no cache')
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_products_with_cached(request):
    # check if cached product is available
    
    if 'product_all' in cache:
        print('Get cache')
        products = cache.get('product_all',)
        # results = [product.to_json() for product in products]
        return Response(products, status=status.HTTP_201_CREATED)
    else:
        print('Write cache')
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        cache.set('product_all', results, timeout=900)
        return Response(results, status=status.HTTP_201_CREATED)


