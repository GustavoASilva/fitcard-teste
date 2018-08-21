from django.contrib import admin
from django.urls import path
from . views import create_establishment
urlpatterns = [
    path('new/', create_establishment, name='create'),
]
