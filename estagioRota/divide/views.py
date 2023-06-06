from django.shortcuts import render
from .divisor import divide
from .models import Produto

# Create your views here.
def index(request): #retorna a view com o formulário de quantos clientes
    return render(request, 'divide/index.html')

def cadastro(request):#retorna a view com o formulário que possui o número de campos requisitado
    if request.method == "GET":
        quantidade = request.GET.__getitem__('pessoas')
        produtos = Produto.objects.all()
        return render(request, 'divide/form.html', {'quantidade': range(0, int(quantidade)), 'produtos': produtos, 'quant': quantidade})
    
def resultado(request):# retorna a view com o resultado final
     if request.method == "POST":
        resultado = divide(request.POST)
        return render(request, 'divide/resultado.html', {"resultado": resultado})
        
    