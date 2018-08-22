from django.shortcuts import render
from django.http import HttpResponse
from . forms import EstablishmentForm
from . models import Establishment
from .serializers import AllEstablishSerializer

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


def create_establishment(request):
    form = EstablishmentForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'establishment_form.html', {'form': form})


class AllEstablishView(APIView):

    def get(self, request):
        establishs = Establishment.objects.all()
        data = AllEstablishSerializer(establishs, many=True)
        return Response(data.data)


def delete_establishment(request, establishment_id):
    establish = get_object_or_404(Establishment, pk= establishment_id)
    if request.method == 'GET':
        establish.delete()
    return Response("ok")


def render_index(request):
    cols = ["RAZAO SOCIAL",
            "CNPJ",
            "CIDADE",
            "ESTADO",
            "TELEFONE",
            "CATEGORIA",
            "AÇÕES"
            ]

    return render(request, 'index.html', {'cols': cols})

class Delete(APIView):

    def post(self, request, establishment_id):
        establish = get_object_or_404(Establishment, pk=establishment_id)
        establish.delete()
        return Response("ok")

