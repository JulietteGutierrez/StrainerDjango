from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):    
    return render(request,'publica/index.html')

def origenes(request):    
    return render(request,'publica/origenes.html')

def tienda(request):    
    return render(request,'publica/tienda.html')