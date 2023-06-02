from django.shortcuts import render
from .Conversor import Conversor

# Create your views here.
def index(request):
    return render(request, 'conversor/index.html')

def resultado(request):
    if request.method == "GET":
        n = request.GET.__getitem__('romano')
        resultado = Conversor.conv(n)
        if type(resultado) == int:
            return render(request, 'conversor/index.html', {'resultado': resultado})
        return render(request, 'conversor/index.html', {'error_message': resultado})
    return render(request, 'conversor/index.html')
    