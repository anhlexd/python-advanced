from django.urls import path
from . import views


urlpatterns = [
      path('', views.OrderListApiView.as_view(), name='home'),
      path('create/', views.OrderListApiView.as_view(), name='add-items'),
      path('all/', views.OrderListApiView.as_view(), name='view_items'),
      path('update/<int:pk>/', views.OrderListApiView.as_view(), name='update-order'),
      path('delete/<int:pk>/', views.OrderListApiView.as_view(), name="delete-order"),
      
]