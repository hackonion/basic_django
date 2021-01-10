from cart.views import cart
from django.urls import path


app_name = 'cart'

urlpatterns = [
    path('', cart.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', cart.cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart.remove, name='cart_remove'),
]

