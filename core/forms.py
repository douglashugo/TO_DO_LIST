from django import forms

class TarefasForm(forms.Form):
    nome=forms.CharField(max_length=80)
    dia=forms.IntegerField()
    mes=forms.IntegerField()

    def clean_nome(self):
        nome=self.cleaned_data['nome']
        return nome.upper()
    
#===========================================
    
from core.models import TodoListModel
from django.forms import ModelForm

class TarefasModelForm(ModelForm):
    class Meta:
        model=TodoListModel
        fields=['nome','dia','mes']

    def clean_nome(self):
        nome=self.cleaned_data['nome']
        return nome.upper()