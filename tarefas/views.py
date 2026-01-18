from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import TarefaForm
from .models import TarefaModel

# Create your views here.
def tarefas_home(request):
    info = {
        'nome': "Matheus",
        'tarefas': TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', info)

def tarefas_add(request: HttpRequest):
    if request.method == 'POST':
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')

    info = {
        'form':TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', info)

def tarefas_del(request: HttpRequest, id: int):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect('tarefas:home')

def tarefas_up(request: HttpRequest, id: int):
    ...