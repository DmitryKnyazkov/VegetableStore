from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import IndexViewLogin


urlpatterns = [
    path('', IndexViewLogin.as_view())]
