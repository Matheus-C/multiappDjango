from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'divide/index.html')

def cadastro(request):
    if request.method == "GET":
        quantidade = request.GET.__getitem__('pessoas')
        return render(request, 'divide/form.html', {'quantidade': range(0, int(quantidade))})
    
def resultado(request):
    pass
        
    