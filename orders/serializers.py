from dataclasses import fields
from msilib.schema import Class
from rest_framework import serializers
from .models import Order

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total_qty',
            'total_price',
            'status',
            
        ]

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total_qty',
            'total_price',
            'status',
            'created',
            'updated',
        ]

#class OrderCreateSerializer(serializers.)