from django.shortcuts import render
from .Conversor import conv

# Create your views here.
def index(request):# retorna a view com o formulário
    return render(request, 'conversor/index.html')

def resultado(request):# retorna para a view inicial com o resultado
    if request.method == "GET":
        n = request.GET.__getitem__('romano')
        resultado = conv(n)
        if type(resultado) == int:
            return render(request, 'conversor/index.html', {'resultado': resultado})
        return render(request, 'conversor/index.html', {'error_message': resultado})
    return render(request, 'conversor/index.html')
    