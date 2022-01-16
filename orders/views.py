from cgitb import lookup
from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderListSerializer, OrderDetailSerializer
from .models import Order

# Create your views here.

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class OrderCrateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class OrderDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Order.objects.all()
    