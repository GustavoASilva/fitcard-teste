from django.db import models
from localflavor.br.models import BRStateField
from . import constants


class Establishment(models.Model):
    razao_social = models.CharField(max_length=30, null=False)
    nome_fantasia = models.CharField(max_length=30)
    cnpj = models.CharField("Número do cnpj", max_length=18, unique=True)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    estado = BRStateField("Estado")
    telefone = models.CharField("Número de telefone", max_length=11, unique=True)
    data_cadastro = models.DateField("Data de cadastro", auto_now=True)
    categoria = models.PositiveIntegerField("Tipo de estabelecimento", choices=constants.CATEGORIES_CHOICES, )
    status = models.BooleanField("Ativo ou Inativo", default=False)
    agencia = models.CharField(name="Agencia bancaria", max_length=5)
    conta = models.CharField(name="Conta bancaria", max_length=8)

    def __str__(self):
        return self.razao_social

