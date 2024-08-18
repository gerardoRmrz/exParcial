from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tema, Articulo
# Create your views here.


def principal(request):
    temasRegistrados = Tema.objects.all().order_by('id')
    return render(request, 'principal.html', {'temasRegistrados':temasRegistrados})

def nuevoTema(request):
    temasRegistrados = Tema.objects.all().order_by('id')
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema = Tema.objects.create(
            nombreTema = nombreTema,
            descripcionTema = descripcionTema
        )
        objTema.save()
        return HttpResponseRedirect( reverse('wikiApp:principal') )
    return render(request, 'nuevoTema.html', {'temasRegistrados':temasRegistrados})

def nuevoArticulo(request):
    temasRegistrados = Tema.objects.all().order_by('id')
    if request.method == 'POST':
        nombreArticulo = request.POST.get('nombreArticulo')
        temaSeleccionado = request.POST.get('temaSeleccionado')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaRelacionado = Tema.objects.get(id=temaSeleccionado)

        objArticulo = Articulo.objects.create(
            nombreArticulo = nombreArticulo,
            contenidoArticulo = contenidoArticulo,
            temaRelacionado=temaRelacionado
        )
        objArticulo.save()

        return HttpResponseRedirect( reverse('wikiApp:principal') )
    return render(request, 'nuevoArticulo.html', {'temasRegistrados':temasRegistrados})

def articulosPorTema(request, idTema):
    temasRegistrados = Tema.objects.all().order_by('id')
    objTema = Tema.objects.get(id=idTema)
    listaArticulos = objTema.articulo_set.all()

    return render(request, 'articulosPorTema.html',{
        'temasRegistrados': temasRegistrados,
        'objTema':objTema,
        'listaArticulos':listaArticulos
    })

def vistaArticulos(request, idArticulo):
    temasRegistrados = Tema.objects.all().order_by('id')
    objArticulo = Articulo.objects.get(id=idArticulo)

    return render(request, 'vistaArticulos.html', {
        'temasRegistrados':temasRegistrados,
        'objArticulo':objArticulo})

def resultadosBusqueda(request):
    temasRegistrados = Tema.objects.all().order_by('id')
    articuloBuscado = request.POST.get('buscarArticulo')
    articuloEncontrado = Articulo.objects.filter(nombreArticulo__contains=articuloBuscado)
    return render(request, 'resultadosBusqueda.html', {
        'temasRegistrados': temasRegistrados,
        'articuloEncontrado':articuloEncontrado})

# artículos por tema
# artículos
# búsqueda: