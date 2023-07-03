from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import IndexViewProduct, IndexViewShop, IndexViewStoreCart, CartViewSet, WishlistView, WishlistViewSet, Wishlistdel

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


app_name = 'store'

urlpatterns = [
    path('', IndexViewShop.as_view(), name='shop'),
    path('cart/', IndexViewStoreCart.as_view(), name='cart'),
    path('product/<int:id>/', IndexViewProduct.as_view(),name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlistdel/<int:id_>', Wishlistdel, name='wishlistdel1')

]