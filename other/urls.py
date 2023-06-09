from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import CurrentDateView, Random_, Hello, IndexView


urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('random/', Random_.as_view()),
    path('hello/', Hello.as_view()),
    path('', IndexView.as_view())
]

