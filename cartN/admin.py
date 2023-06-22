from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartN, CartItem, Product1

# admin.site.register(CartN)
admin.site.register(CartItem)
admin.site.register(Product1)

