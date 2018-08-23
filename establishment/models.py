from django.db import models
from localflavor.br.models import BRStateField
from . import constants


class Establishment(models.Model):
    razao_social = models.CharField(max_length=30, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=30, null=True, blank=True)
    cnpj = models.CharField("Número do cnpj", max_length=18, unique=True)
    email = models.EmailField()
    endereco = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=30, null=True, blank=True)
    estado = BRStateField("Estado")
    telefone = models.CharField("Número de telefone", max_length=15, unique=True, null=True, blank=True)
    data_cadastro = models.DateField("Data de cadastro", null=True, blank=True)
    categoria = models.PositiveIntegerField("Tipo de estabelecimento", choices=constants.CATEGORIES_CHOICES, )
    status = models.BooleanField("Ativo ou Inativo", default=True)
    agencia = models.CharField("Agencia", max_length=5, null=True, blank=True)
    conta = models.CharField("Conta", max_length=8, null=True, blank=True)

    class Meta:
        ordering = ('-razao_social',)
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabeleciemntos'

    def __str__(self):
        return self.razao_social

    def save(self, *args, **kwargs):
        super(Establishment, self).save(*args, **kwargs)

    def get_category_display(self):
        for code, label in constants.CATEGORIES_CHOICES:
            if self.categoria == code:
                return label
