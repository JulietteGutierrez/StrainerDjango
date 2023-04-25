from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('origenes/',views.origenes,name='origenes'), 
    path('sucursales/',views.sucursales,name='sucursales'), 
    path('tienda-online/',views.tienda,name='tienda-online'),
]