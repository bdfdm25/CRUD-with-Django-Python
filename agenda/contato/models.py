# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contato(models.Model):

  #dados do seletor 'sexo'
  SEXO_CHOICES = (
    (u'masculino', u'Masculino'),
    (u'feminino' , u'Feminino'),
    )

  #dados do seletor 'estado_civil'
  ESTADO_CIVIL_CHOICES = (
    (u'solteiro', u'Solteiro'),
    (u'casado' , u'Casado'),
    (u'divorciado', u'Divorciado'),
    (u'viuvo', u'Viuvo')
    )

  #campos da tabela
  contato_id = models.AutoField(primary_key = True)
  contato_nome = models.CharField(max_length = 45)
  contato_nascimento = models.DateField()
  contato_sexo = models.CharField(max_length = 50, choices = SEXO_CHOICES)
  contato_estado_civil = models.CharField(max_length = 50, choices = ESTADO_CIVIL_CHOICES, verbose_name = 'Estado Civil')
  contato_email = models.CharField(max_length = 50)
  contato_favorito= models.BooleanField(verbose_name = 'Favorito')


class Tarefa(models.Model):

  tarefa_id = models.AutoField(primary_key = True)
  tarefa_nome = models.CharField(max_length = 120)
  tarefa_descricao_inicio = models.DateField()
  concluido = models.BooleanField(verbose_name = 'Concluido')


class Conta(models.Model):

  conta_id = models.AutoField(primary_key = True)
  conta_nome = models.CharField(max_length = 200)
  conta_data_vencimento = models.DateField()
  pago = models.BooleanField(verbose_name = 'Pago')

