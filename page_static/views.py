from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contatos.html')

def sobre(request):
    return render(request, 'sobre.html')

def Servicos(request):
    return render(request, 'servicos.html')