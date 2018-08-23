from django.forms import ModelForm
from django import forms

from .models import Establishment


class EstablishmentForm(ModelForm):
    cnpj = forms.CharField(max_length=18, min_length=18)
    agencia = forms.CharField(max_length=5, min_length=5)
    conta = forms.CharField(max_length=8, min_length=8)
    telefone = forms.CharField(max_length=15, min_length=15, required=False)

    def __init__(self, *args, **kwargs):
        super(EstablishmentForm, self).__init__(*args, **kwargs)
        self.fields['cnpj'].label = "CNPJ (Obrigatório)"
        self.fields['razao_social'].label = "Razão Social (Obrigatório)"


    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        if categoria == 1:
            if cleaned_data.get('telefone') == '':
                raise forms.ValidationError('Supermercado obrigatorio o telefone!!!')

    class Meta:
        model = Establishment
        fields = '__all__'
        exclude = ('status',)

