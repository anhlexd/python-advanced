from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def _str__(self):
        return self.name

