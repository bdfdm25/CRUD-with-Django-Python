# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('contato_id', models.AutoField(primary_key=True, serialize=False)),
                ('contato_nome', models.CharField(max_length=45)),
                ('contato_nascimento', models.DateField()),
                ('contato_sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=50)),
                ('contato_estado_civil', models.CharField(choices=[('solteiro', 'Solteiro'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viuvo', 'Viuvo')], max_length=50, verbose_name='Estado Civil')),
                ('contato_email', models.CharField(max_length=50)),
                ('contato_favorito', models.BooleanField(verbose_name='Favorito')),
            ],
        ),
    ]
