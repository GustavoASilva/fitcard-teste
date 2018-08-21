from django.shortcuts import render
from django.http import HttpResponse
from . forms import EstablishmentForm
from . models import Establishment
from .serializers import AllEstablishSerializer

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

def example(request):
    return render(request, 'index.html')