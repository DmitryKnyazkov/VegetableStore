from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import IndexViewProduct, IndexViewShop, IndexViewStoreCart


urlpatterns = [
    path('product/', IndexViewProduct.as_view()),
    path('', IndexViewShop.as_view()),
    path('cart/', IndexViewStoreCart.as_view()),]