from django.db import models
from datetime import date

class TodoListModel(models.Model):
    nome = models.CharField('Tarefa', max_length=80)
    dia = models.IntegerField('Dia')
    mes = models.IntegerField('Mês')
    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def get_data(self):
        # assume que o ano da ativadade é do ano corrente
        ano_atual = date.today().year
        return date(ano_atual, self.mes, self.dia)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name='Tarefa'
        verbose_name_plural='Tarefas'
        ordering=('mes','-dia')
