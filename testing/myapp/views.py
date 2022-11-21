from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from myapp.models import TODOList
from myapp.serializers import TODOSerializer
from myapp.permissions import IsOwnwe

# Create your views here.

class TODOListView(ListCreateAPIView):
    queryset = TODOList.objects.all()
    serializer_class = TODOSerializer
    permission_classes = (IsAuthenticated)

class TODODetailView(RetrieveUpdateDestroyAPIView):
    queryset = TODOList.objects.all()
    serializer_class = TODOSerializer
    permission_classes = (IsOwnwe, )
