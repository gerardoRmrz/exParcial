from django.urls import path, include
from . import views
app_name = 'wikiApp'



urlpatterns = [
    path('', views.principal, name='principal'),
    path('nuevoTema', views.crearNuevoTema, name='crearNuevoTema' ),
    path('nuevoArticulo', views.crearNuevoArticulo, name='crearNuevoArticulo'),
    path('articuloPorTema', views.articuloPorTema, name='articuloPorTema'),
    path('articulos', views.articulos, name='articulos'),
    path('busqueda', views.busqueda, name='busqueda')
]
