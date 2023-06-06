from django.db import models

# Create your models here.
class Produto(models.Model):# definição da classe produto e da tabela produto no banco de dados
    nome = models.CharField(max_length=100)
    preco = models.FloatField()

    def getPreco(self):
        return self.preco
    def __str__(self):
        return '{} ({})'.format(self.nome, self.preco)
