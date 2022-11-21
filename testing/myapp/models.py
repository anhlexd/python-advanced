from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODOList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified= models.DateField(auto_now=True)

    def __str__(self):
        return self.name