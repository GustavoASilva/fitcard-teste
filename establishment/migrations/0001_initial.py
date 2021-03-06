# Generated by Django 2.1 on 2018-08-23 02:07

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=30)),
                ('nome_fantasia', models.CharField(blank=True, max_length=30, null=True)),
                ('cnpj', models.CharField(max_length=18, unique=True, verbose_name='Número do cnpj')),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', localflavor.br.models.BRStateField(max_length=2, verbose_name='Estado')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Número de telefone')),
                ('data_cadastro', models.DateField(blank=True, null=True, verbose_name='Data de cadastro')),
                ('categoria', models.PositiveIntegerField(choices=[(1, 'Supermercado'), (2, 'Restaurante'), (3, 'Borracharia'), (4, 'Oficina'), (5, 'Posto')], verbose_name='Tipo de estabelecimento')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo ou Inativo')),
                ('agencia', models.CharField(blank=True, max_length=5, null=True, verbose_name='Agencia')),
                ('conta', models.CharField(blank=True, max_length=8, null=True, verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'Estabelecimento',
                'verbose_name_plural': 'Estabeleciemntos',
                'ordering': ('-razao_social',),
            },
        ),
    ]
