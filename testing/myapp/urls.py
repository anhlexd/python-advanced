from django.urls import path
from myapp.views import TODOListView, TODODetailView

urlpatterns = [
    path('todo/', TODOListView.as_view(), name='todo'),
    path('todo/<str:pk>/', TODODetailView.as_view(), name='todo-detail')
]