from django.contrib import admin
from .models import Order, StatusOrder, ItemInOrder
# Register your models here.

admin.site.register(Order)
admin.site.register(StatusOrder)
admin.site.register(ItemInOrder)