from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tarefas_home(request):
    return render(request, 'tarefas/home.html')

def tarefas_add(request):
    return HttpResponse('Adicione aki suas tarefas!')