from django.urls import path
from . views import create_establishment, delete_establishment, AllEstablishView, render_index, Delete


urlpatterns = [
    path('new/', create_establishment, name='create'),
    path('delete/<int:establishment_id>', delete_establishment, name='delete'),
    path('api/all/', AllEstablishView.as_view()),
    path('api/delete/<int:establishment_id>', Delete.as_view()),
    path('index', render_index, name='render_index'),
]
