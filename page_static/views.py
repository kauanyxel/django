from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>views test""</h1>")

def contato(request):
    return HttpResponse("<p>telefone:(21)96546-64987</p><p>Email:ababoi@gmail""<p>")