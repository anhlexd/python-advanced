import os
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings");
django.setup()

from pagination.models import Customer

Customer.objects.create(name='Tuan Anh1', country='Viet Nam')
Customer.objects.create(name='Tuan Anh2', country='Viet Nam')
Customer.objects.create(name='Tuan Anh3', country='Viet Nam')
Customer.objects.create(name='Tuan Anh4', country='Viet Nam')
Customer.objects.create(name='Tuan Anh5', country='Viet Nam')
Customer.objects.create(name='Tuan Anh6', country='Viet Nam')
Customer.objects.create(name='Tuan Anh7', country='Viet Nam')
Customer.objects.create(name='Tuan Anh8', country='Viet Nam')
