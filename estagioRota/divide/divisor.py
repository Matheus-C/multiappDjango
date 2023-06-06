import re
from .models import Produto
from django.shortcuts import get_object_or_404

class Cliente:# classe do objeto cliente
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

    def calculaServico(self):# calcula a taxa de 10% de acordo com o gasto daquela pessoa
        self._total = self._total + self._total*0.1
    
    def __str__(self):# função para definir a representação da classe
        return "{} = R$ {:.2f}".format(self._nome, self._total)
        

def divide(dados):# função que agrupa os items com os clientes e faz a divisão
    clientes = []
    n = int(dados.__getitem__("quant"))
    for i in range(n):
        produtos = []
        prodPorCliente = []
        for dado in list(dados.keys()):
            if re.match("^C{}P.".format(i), dado):
                prodPorCliente.append(dado)
        for j in range(len(prodPorCliente)):
            p = int(dados.__getitem__("C{}P{}".format(i, j)))
            if p != -1:
                produtos.append(p)
        if dados.get("servico{}".format(i), False) == "on":
            servico = True
        else:
            servico = False
        clientes.append(Cliente(dados.__getitem__("nome{}".format(i)), servico, produtos))#agrupa os clientes com os produtos
        
    prod = []
    for i in range(n):
        prod.append(clientes[i].getProdutos())
    prod = [item for sublist in prod for item in sublist]
    newProd = list(set(prod))
    nClientesConsumo = {}
    for i in range(len(newProd)):
        nClientesConsumo[newProd[i]] = prod.count(newProd[i])
    for i in range(n):
        prodCliente = clientes[i].getProdutos()
        total = 0
        for j in range(len(prodCliente)):
            total = total + (get_object_or_404(Produto, pk=prodCliente[j]).getPreco()/nClientesConsumo[prodCliente[j]])
        clientes[i].setTotal(total)
        if clientes[i].getServico():
            clientes[i].calculaServico()
    #calcula o valor para cada cliente
    return clientes


