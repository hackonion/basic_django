from django.urls import path
from orders.views import orders

app_name = 'orders'

urlpatterns = [
    path('create/', orders.order_create, name='order_create'),
]
