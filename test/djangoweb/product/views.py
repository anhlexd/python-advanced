from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serlializers import ProductSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_product': '/',
        'search by name' : '/?name=product_name',
        'search by price' : '/?price=product_price',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_product (request):
    product = ProductSerializer(data=request.data)

    # validating for already existing data
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_product(request):

    # checking for the parameters from the URL
    if request.query_params:
        product = Product.objects.filter(**request.query_param.dict())
    else:
        product = Product.objects.all()

    # if there is something in items else raise error
    if product:
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_202_ACCEPTED)