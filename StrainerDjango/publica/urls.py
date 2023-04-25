from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('origenes/',views.origenes,name='origenes'), 
    path('sucursales/',views.sucursales,name='sucursales'), 
<<<<<<< HEAD
    path('tienda-online/',views.tienda,name='tienda-online'),
    path('contacto/',views.contacto,name='contacto'),
=======
    path('contacto/',views.contacto,name='contacto'),
    path('tienda/',views.tienda,name='tienda'),
    path('tienda/producto/<int:id>', views.tiendaProducto, name='producto'),
    # path('tienda/carrito/<int:id>/<str:cantidad>', views.tiendaCarritoAgregar, name='carritoAgregar'),
>>>>>>> de9a26272c4f020ac8392e943a996a460db1903f
]