from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from .models import Order, OrderItem
from .serlializers import OrderItemSerializer, OrderSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import permissions


# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_infor_order': '/',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }

#     return Response(api_urls)

# def map_order_product_item_query(order, product_list):

#     def map_order_product_item(product):
#         return OrderItem(
#             product_name = product["product_name"],
#             product_price = product["product_price"],
#             quantity = product["quantity"],
#             total_price = product["total_price"],
#             order = order
#         )

#     return list(map(map_order_product_item, product_list))

# @api_view(['POST'])
# @transaction.atomic
# def add_orderitem (request):
#     item = OrderItemSerializer(data=request.data)

#     # save infor customer into order table
#     new_order = Order.objects.create(
#             customer_name = request.data["customer_name"],
#             customer_phone = request.data["customer_phone"],
#             customer_address = request.data["customer_address"]
#         )

#     product_list = request.data["product"]
#     list_order_product_query = map_order_product_item_query(new_order, product_list)
#     OrderItem.objects.bulk_create(list_order_product_query)

#     return Response(status=status.HTTP_200_OK)


# def map_product_item(order):
#     product_list = OrderItem.objects.filter(order_id=order["id"]).values()
#     order["product"] = product_list
#     return order

# @api_view(['GET'])
# def view_order(request):
#     order_list = Order.objects.all().values()
#     data = list(map(map_product_item, order_list))
#     return Response(data=data)

# @api_view(['PUT'])
# def update_order(request, pk):
#     order_list = Order.objects.get(pk=pk) 
#     print("::order_list",order_list)
    
#     if not order_list:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     data = {
#         "customer_name": request.data.get('customer_name'),
#         "customer_phone": request.data.get('customer_phone'),
#         "customer_address": request.data.get('customer_address')

#     }

#     serializer = OrderSerializer(instance=order_list, data=data, partial = True )
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_order(request, pk):
#     order_list = Order.objects.get(pk=pk) 
#     if not order_list:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     order_list.delete()

#     return Response(status=status.HTTP_202_ACCEPTED)


##########################

def map_order_product_item_query(order, product_list):

    def map_order_product_item(product):
        return OrderItem(
            product_name = product["product_name"],
            product_price = product["product_price"],
            quantity = product["quantity"],
            total_price = product["total_price"],
            order = order
        )

    return list(map(map_order_product_item, product_list))

def map_product_item(order):
    product_list = OrderItem.objects.filter(order_id=order["id"]).values()
    order["product"] = product_list
    return order

class OrderListApiView(APIView):

    def get(self, request, *args, **kwargs):
        order_list = Order.objects.all().values()
        data = list(map(map_product_item, order_list))
        return Response(data=data)
       
    # create

    @transaction.atomic
    def post(self, request, *args, **kwargs):
       
        new_order = Order.objects.create(
                customer_name = request.data["customer_name"],
                customer_phone = request.data["customer_phone"],
                customer_address = request.data["customer_address"]
            )

        product_list = request.data["product"]

        list_order_product_query = map_order_product_item_query(new_order, product_list)

        OrderItem.objects.bulk_create(list_order_product_query)

        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        order_list = Order.objects.get(pk=pk) 

        if not order_list:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        data = {

            "customer_name": request.data.get('customer_name'),
            "customer_phone": request.data.get('customer_phone'),
            "customer_address": request.data.get('customer_address')

        }

        serializer = OrderSerializer(instance=order_list, data=data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete_order(self, request, pk, *args, **kwargs):
        order_list = self.get_objects(pk, request.order.id)

        if not order_list:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        order_list.delete()

        return Response(status=status.HTTP_202_ACCEPTED)