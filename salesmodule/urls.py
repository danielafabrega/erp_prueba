from django.urls import path

from . import views

app_name = 'salesmodule'
urlpatterns = [
    #path('', views.index, name='index'),
    path('busqueda_productos/', views.busqueda_productos, name='busqueda_productos'),
    path('buscar/', views.buscar, name="buscar"),
    
]