from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefas_home(request):
    contexto = {
        'nome': 'Matheus',
        'idade': 19 
    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_add(request):
    return HttpResponse('Adicione aki suas tarefas')