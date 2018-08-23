from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import EstablishmentForm
from . models import Establishment
from .serializers import AllEstablishSerializer

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


def create_establishment(request):
    form = EstablishmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('render_index')
    return render(request, 'establishment_form.html', {'form': form})


def update_establishment(request, establishment_id):
    establish = get_object_or_404(Establishment, pk=establishment_id)
    form = EstablishmentForm(request.POST or None, instance=establish)
    if form.is_valid():
        form.save()
        return redirect('render_index')

    return render(request, 'establishment_form.html', {'form': form})





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


class AllEstablishView(APIView):
    def get(self, request):
        establishs = Establishment.objects.all()
        data = AllEstablishSerializer(establishs, many=True)
        return Response(data.data)


class DeleteEstablishmentApi(APIView):
    def post(self, request, establishment_id):
        establish = get_object_or_404(Establishment, pk=establishment_id)
        establish.delete()
        return Response("ok")

