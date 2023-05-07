from django.shortcuts import render, redirect
from .forms import TarefasForm
from datetime import date
from .models import TodoListModel

def index(request):
    hoje = date.today()
    dia_atual = hoje.day
    mes_atual = hoje.month

    tarefas = TodoListModel.objects.filter(dia=dia_atual, mes=mes_atual)

    return render(request, 'index.html', {'tarefas': tarefas})


def cadastro(request):
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TarefasForm()
    return render(request, 'cadastro.html', {'form': form})