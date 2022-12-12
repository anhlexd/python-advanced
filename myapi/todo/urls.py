from django.urls import path, include
from .views import TodoListAPIView, TodoDetailAPIView

urlpatterns = [
    path('api/', include('todo.api.urls')),
    path('api/', TodoListAPIView.as_view()),
    path('api/<int:pk>/', TodoDetailAPIView.as_view()),
]