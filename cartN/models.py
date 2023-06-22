from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class CartN(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user}"
#
#
class Product1(models.Model):
   name = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   description = models.TextField()
   image = models.ImageField(upload_to='static/products/', null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name
#
#
class CartItem(models.Model):
   cart = models.ForeignKey(CartN, on_delete=models.CASCADE)
   product = models.ForeignKey(Product1, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.cart}_{self.product}"
