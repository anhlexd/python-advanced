from django.urls import path
from . import views

urlpatterns = [
      path('', views.ApiOverview, name='home'),
      path('create/', views.add_product, name='add-items'),
      path('all/', views.view_product, name='view_product'),
      path('update/<int:pk>/', views.update_product, name='update-product'),
      path('item/<int:pk>/delete/', views.delete_product, name='delete-product'),
]