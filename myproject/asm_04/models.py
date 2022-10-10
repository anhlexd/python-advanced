from django.db import models
from django.forms import ModelForm

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    color = models.CharField(max_length=50)

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'age', 'color']
