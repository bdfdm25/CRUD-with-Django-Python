# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from agenda.contato.models import Contato, Tarefa, Conta

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
  model = Contato
  
  #forma de exibicao dos dados na tabela
  list_display = ['contato_nome', 'contato_email', 'contato_favorito']
  
  #filtro de pesquisa dos registros
  list_filter = ['contato_sexo', 'contato_estado_civil']
  
  #filtro de pesquisa padrao no campo 'pesquisa'
  search_fields = ['contato_nome']
  
  #habilita o botao salvar na parte superior da pagina
  save_on_top = True

admin.site.register(Contato, ContatoAdmin)

class TarefaAdmin(admin.ModelAdmin):
  model = Tarefa

  list_display = ['tarefa_nome', 'tarefa_descricao_inicio', 'concluido']
  search_fields = ['tarefa_nome']
  save_on_top = True
admin.site.register(Tarefa, TarefaAdmin) 

class ContaAdmin(admin.ModelAdmin):
  model = Conta

  list_display = ['conta_nome', 'conta_data_vencimento', 'pago']
  search_fields = ['conta_nome']
  list_filter = ['pago']
  save_on_top = True
admin.site.register(Conta, ContaAdmin)
