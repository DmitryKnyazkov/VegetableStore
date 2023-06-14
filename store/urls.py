from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import IndexViewProduct, IndexViewShop, IndexViewStoreCart

app_name = 'store'

urlpatterns = [
    path('', IndexViewShop.as_view(), name='shop'),
    path('cart/', IndexViewStoreCart.as_view(), name='cart'),
    path('product/<int:id>/', IndexViewProduct.as_view(),name='product')]