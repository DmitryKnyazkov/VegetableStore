from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.views import View
from django.http import HttpResponse


class IndexViewStoreCart(View):
    def get(self, request):
       return render(request, 'store/cart.html')

class IndexViewProduct(View):
   def get(self, request):
       return render(request, 'store/product-single.html')

class IndexViewShop(View):
   def get(self, request):
       context = {'data': [{'name': 'Bell Pepper',
                            'discount': 30,
                            'price_before': 120.00,
                            'price_after': 80.00,
                            'url': 'store/images/product-1.jpg'}
                           ]
                  }
       return render(request, 'store/shop.html', context)