from django.db import models
from customer.models import User

# Create your models here.
class Order(models.Model):
    price = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_order", null=True)

    class Meta :
        db_table = "Oder"

class OrderItem(models.Model):
    product_name        = models.CharField(max_length=255)
    product_price       = models.IntegerField(default=0)
    quantity            = models.IntegerField(default=0)
    total_price         = models.IntegerField(default=0)
    order               = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="OrderItem_order")

    class Meta :
        db_table = "OrderItem"




