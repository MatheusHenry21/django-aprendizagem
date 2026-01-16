from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tarefas_home(request):
    info = {
        'nome': "Matheus",
        'idade': 20
    }
    return render(request, 'tarefas/home.html', info)

def tarefas_add(request):
    return HttpResponse('Adicione aki suas tarefas!')