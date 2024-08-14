from django.urls import path, include
from . import views
app_name = 'wikiApp'



urlpatterns = [
    path('', views.inicio, name='inicio')
]