from django.contrib import admin

# Register your models here.
from .models import Product, Category, Discount


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
