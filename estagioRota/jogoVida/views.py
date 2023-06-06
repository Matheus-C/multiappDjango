from django.shortcuts import render
from .jogo import novoJogo, rodada
# Create your views here.

def index(request):# view inicial
    return render(request, 'jogoVida/index.html')

def novo(request):# view com um novo tabuleiro gerado aleatóriamente
    matriz = novoJogo()
    return render(request, 'jogoVida/index.html', {'matriz': matriz})

def proximo(request, matriz):# view com a próxima rodada(geração)
    prox = rodada(matriz)
    return render(request, 'jogoVida/index.html', {'matriz': prox})