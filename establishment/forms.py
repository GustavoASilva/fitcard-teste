from django.forms import ModelForm
from .models import Establishment


class EstablishmentForm(ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'

