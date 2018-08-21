from django.urls import path
from . views import create_establishment, AllEstablishView, example


urlpatterns = [
    path('new/', create_establishment, name='create'),
    path('api/all/', AllEstablishView.as_view()),
    path('index', example),
]
