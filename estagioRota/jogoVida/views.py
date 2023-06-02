from django.shortcuts import render
from .jogo import novoJogo, rodada
# Create your views here.

def index(request):
    return render(request, 'jogoVida/index.html')

def novo(request):
    matriz = novoJogo()
    return render(request, 'jogoVida/index.html', {'matriz': matriz})

def proximo(request, matriz):
    prox = rodada(matriz)
    return render(request, 'jogoVida/index.html', {'matriz': prox})