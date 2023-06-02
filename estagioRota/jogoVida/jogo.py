import random
import ast

def novoJogo():
    tabuleiro = []
    for i in range(4):
        tabuleiro.append([])
        for j in range(4):
            tabuleiro[i].append(random.randint(0, 1))
    return tabuleiro

def quantosVizinhos(x, y, tab):
    vizinhos = 0
    for i in range(x-1, x+2, 2):
        if 0 <= i < len(tab):
            if tab[i][y] == 1:
                vizinhos = vizinhos + 1
    for j in range(y-1, y+2, 2):
        if 0 <= j < len(tab[0]):
            if tab[x][j] == 1:
                vizinhos = vizinhos + 1
    for i in range(x-1, x+2, 2):
        if 0 <= i < len(tab):
            for j in range(y-1, y+2, 2):
                if 0 <= j < len(tab[0]):
                    if tab[i][j] == 1:
                        vizinhos = vizinhos + 1
    return vizinhos

def rodada(tab):
    tabuleiro = ast.literal_eval(tab)
    aux = []
    for i in range(4):
        aux.append([])
        for j in range(4):
            aux[i].append(0)
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            vizinhos = quantosVizinhos(i, j, tabuleiro)
            aux[i][j] = vizinhos
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if aux[i][j] == 3:
                tabuleiro[i][j] = 1
            elif aux[i][j] < 2:
                tabuleiro[i][j] = 0
            elif aux[i][j] > 3:
                tabuleiro[i][j] = 0
    return tabuleiro
