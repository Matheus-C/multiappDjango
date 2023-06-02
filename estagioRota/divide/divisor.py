class Cliente:
    def __init__(self, nome, servico, consumiu):
        self._nome = nome
        self._servico = servico
        self._consumiu = consumiu
        self._total = 0
    
    def getNome(self):
        return self._nome
    def getservico(self):
        return self._servico
    def getConsumiu(self):
        return self._consumiu
    def getTotal(self):
        return self._total
    def setTotal(self, total):
        self._total = total
    def calculaServico(self):
        if self._servico:
            return self._total+(self._total*0.1)

class produto:
    def __init__(self, nome, valor, n):
        self._nome = nome
        self._valor = valor
        self._nClientes = n
        self._valorFinal = 0
    def getNome(self):
        return self._nome
    def getValor(self):
        return self._valor
    def getClientes(self):
        return self._nClientes
    def setClientes(self, nomes):
        self._nClientes = nomes
    def setNome(self, nome):
        self._nome = nome
    def setValor(self, valor):
        self._valor = valor
    def adicionaCliente(self):
        self._nClientes =+ 1
    def calcula(self):
        self._valorFinal = self._valor/self._nClientes


