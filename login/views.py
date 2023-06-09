from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.views import View
from django.http import HttpResponse


class IndexViewLogin(View):
    def get(self, request):
       return render(request, 'login/index.html')

    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={"indent": 4})