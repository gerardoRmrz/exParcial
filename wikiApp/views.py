from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def principal(request):
    temasRegistrados = [ f'Tema {x}' for x in range(7) ]
    return render(request, 'principal.html', {'temasRegistrados':temasRegistrados})

def crearNuevoTema(request):
    return HttpResponse("Bienvenido a crear nuevo tema")

def crearNuevoArticulo(request):
    return HttpResponse('Bienvenido a crearNuevoArticulo')

def articuloPorTema(request):
    return HttpResponse('Bienvenido a articulo por tema')

def articulos(request):
    return HttpResponse('Bienvenido a articulos')

def busqueda(request):
    return HttpResponse('Bienvenido a búsqueda')

# artículos por tema
# artículos
# búsqueda: