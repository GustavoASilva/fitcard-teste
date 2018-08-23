from django.urls import path
from . views import create_establishment, update_establishment, AllEstablishView, render_index, DeleteEstablishmentApi


urlpatterns = [

    path('new/', create_establishment, name='create'),
    path('edit/<int:establishment_id>', update_establishment, name='update'),
    path('api/all/', AllEstablishView.as_view()),
    path('api/delete/<int:establishment_id>', DeleteEstablishmentApi.as_view()),
]
