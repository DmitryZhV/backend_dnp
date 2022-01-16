from django.urls import path

from . import views

urlpatterns = [ path('orders/', views.OrderListAPIView.as_view(), name="order_list"),
                path('order/<int:id>/', views.OrderRetrieveAPIView.as_view(), name="order_detail"), 
                path('create/', views.OrderCrateAPIView.as_view(), name="order_create"), 
                path('delete/<int:id>/', views.OrderDestroyAPIView.as_view(), name="order_delete"),]