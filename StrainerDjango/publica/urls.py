from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('origenes/',views.origenes,name='origenes'), 
    path('sucursales/',views.sucursales,name='sucursales'), 
    path('contacto/',views.contacto,name='contacto'),
    path('tienda/',views.tienda,name='tienda'),
    path('tienda/producto/<int:id>', views.tiendaProducto, name='producto'),
    # path('tienda/carrito/<int:id>/<str:cantidad>', views.tiendaCarritoAgregar, name='carritoAgregar'),
]