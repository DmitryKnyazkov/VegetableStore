from django.shortcuts import render

# Create your views here.

from datetime import datetime


from django.views import View
from django.http import HttpResponse

from random import random

from django.shortcuts import render

class IndexView(View):
   def get(self, request):
       return render(request, 'other/index.html')

class CurrentDateView(View):
   def get(self, request):
       html = f"{datetime.now()}"
       return HttpResponse(html)

class Random_(View):
    def get(self, request):
        html = f"{random()}"
        return HttpResponse(html)

class Hello(View):
    def get(self, request):
        html = """<h1>Hello, World</h1>"""
        return HttpResponse(html)