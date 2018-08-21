from django.shortcuts import render
from django.http import HttpResponse
from . forms import EstablishmentForm


def create_establishment(request):
    form = EstablishmentForm(request.POST, None)
    import ipdb;ipdb.set_trace()
    if form.is_valid():
        form.save()
    return render(request, 'establishment_form.html', {'form': form})
