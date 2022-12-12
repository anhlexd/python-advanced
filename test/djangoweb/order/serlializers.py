from django.db.models import fields
from rest_framework import serializers
from .models import Order, OrderItem 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("price", "customer_name", "customer_phone", "customer_address")

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product_name", "product_price", "quantity", "total_price", "order")