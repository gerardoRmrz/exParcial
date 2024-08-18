from django.urls import path, include
from . import views
app_name = 'wikiApp'



urlpatterns = [
    path('', views.principal, name='principal'),
    path('nuevoTema', views.nuevoTema, name='nuevoTema' ),
    path('nuevoArticulo', views.nuevoArticulo, name='nuevoArticulo'),
    path('articulosPorTema/<str:idTema>', views.articulosPorTema, name='articulosPorTema'),
    path('vistaArticulos/<str:idArticulo>', views.vistaArticulos, name='vistaArticulos'),
    path('resultadosBusqueda', views.resultadosBusqueda, name='resultadosBusqueda')
]
