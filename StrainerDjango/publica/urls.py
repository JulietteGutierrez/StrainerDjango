from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('origenes/',views.origenes,name='origenes'), 
    path('sucursales/',views.sucursales,name='sucursales'),
    path('contacto/',views.contacto,name='contacto'),  
    path('tienda-online/',views.tienda,name='tienda-online'),
    path('tienda-online/producto/<int:id>', views.tiendaProducto, name='producto'),
    path('tienda-online/carrito/<int:id>/<int:cantidad>', views.tiendaCarritoAgregar, name='carrito'),
]