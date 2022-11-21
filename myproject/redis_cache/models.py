from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length = 255, blank = True)
    price= models.DecimalField(max_digits = 10, decimal_places = 2)
    date_created = models.DateTimeField(auto_now_add=True, blank = True)
    date_modified = models.DateTimeField(auto_now=True, blank= True)

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'description':self.description,
            'price': self.price,
            'date_created': self.date_created,
            'date_modified': self.date_modified

        }