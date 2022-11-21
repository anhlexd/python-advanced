from django.urls import path
from .views import show_info

urlpatterns = [
    path('<str:name>/',show_info),
]