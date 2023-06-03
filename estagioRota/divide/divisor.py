import re
from .models import Produto
from django.shortcuts import get_object_or_404

class Cliente:
    def __init__(self, nome = "" , servico = False, produtos = []):
        self._nome = nome
        self._servico = servico
        self._produtos = produtos
        self._total = 0.0
    
    def setNome(self, nome):
        self._nome = nome
    def setServico(self, servico):
        self._servico = servico
    def setProdutos(self, produtos):
        self._produtos = produtos
    def setTotal(self, total):
        self._total = total
    
    def getNome(self):
        return self._nome
    def getServico(self):
        return self._servico
    def getProdutos(self):
        return self._produtos
    def getTotal(self):
        return self._total
    
    def __str__(self):
        return "{self._nome} = {self._total}"
        

def divide(dados):
    clientes = []
    n = int(dados.__getitem__("quantidade"))
    for i in range(n):
        produtos = []
        prodPorCliente = re.findall("^C{i}P.", dados.keys())
        for j in range(len(prodPorCliente)):
            produtos.append(int(dados.__getitem__("C{i}P{j}")))
        clientes.append(Cliente(dados.__getitem__("nome{i}"), dados.__getitem__("servico{i}"), produtos))
    prod = []
    for i in range(n):
        prod.append(clientes[i].getProdutos())
    prod = [item for sublist in prod for item in sublist]
    newProd = set(prod)
    nClientesConsumo = {}
    for i in range(len(newProd)):
        nClientesConsumo[newProd[i]] = prod.count(newProd[i])
    for i in range(n):
        prodCliente = clientes[i].getProdutos()
        total = 0
        for j in range(len(prodCliente)):
            total = total + (get_object_or_404(Produto, pk=prodCliente[j]).getPreco()/nClientesConsumo[prodCliente[j]])
        clientes[i].setTotal(total)
    
    return clientes


