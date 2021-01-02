from shop.views import Product
from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', Product.product_list, name='product_list'),
    path('<slug:category_slug>/', Product.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', Product.product_detail, name='product_detail'),
]