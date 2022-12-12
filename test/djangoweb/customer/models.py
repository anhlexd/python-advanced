from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.username
