from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from publica.forms import ContactoForm
from django.contrib import messages

# Create your views here.
def index(request):    
    return render(request, 'publica/index.html')

def origenes(request):    
    return render(request,'publica/origenes.html')

def sucursales(request):    
    return render(request,'publica/sucursales.html')

def contacto(request):
    # mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)    
        # mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')          
        # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        #Cuando recibo el formulario por el metodo GET (cuando cargo la pagina)
        #Creo un formulario vacio
        contacto_form = ContactoForm()

    context = {
        'contacto_form': contacto_form
    }
    return render(request,'publica/contacto.html',context)

def tienda(request):    
    return render(request, 'publica/tienda.html', getContextoTienda())

def getContextoTienda():
    return {
        "categorias": getDictCategorias(),
        "productos": getDictProductos(),
    } 

def tiendaProducto(request, id):
    return render(request, 'publica/producto.html', getContextoProducto(id))

def getContextoProducto(id):
    return {
        "producto": getDictProducto(id),
    } 

# def tiendaCarritoAgregar(request, id, cantidad=0):
#     return tienda(request)

#########################################################################
#                                                                       #
# Cuando agreguemos la Base de Datos las siguientes funciones vuelan... #
#                                                                       #
#########################################################################

def getDictCategorias():
    selectDistinctCategoriasFromProductos = []
    for n in range(1, 6):
        selectDistinctCategoriasFromProductos.append(formatDictCategoria(n))
    return selectDistinctCategoriasFromProductos

def formatDictCategoria(id):
    return {"id": id, "categoria": getCategoria(id)}

def getCategoria(id):
    categorias = ("Cafeteras", "Cápsulas", "Merchandising", "Packs", "Soportes")
    if (id > 0) and (id <= len(categorias)):
        return categorias[id-1]
    else:
        return "*** ERROR ***"

def getDictProductos():
    selectProductosFromProductosYCategorias = []
    for id in range(1,14):
        selectProductosFromProductosYCategorias.append(getDictProducto(id))
    return selectProductosFromProductosYCategorias

def getDictProducto(id):
    (id, nombre, precio, id_categoria, imagen, descripcion) = getProducto(id)
    return formatDictProducto(id, nombre, precio, id_categoria, imagen, descripcion)

def formatDictProducto(id, nombre, precio, id_categoria, imagen, descripcion):
    return {
            "id": id,
            "nombre": nombre,
            "precio": precio, 
            "id_categoria": id_categoria, 
            "categoria": getCategoria(id_categoria),
            "imagen": imagen,
            "descripcion": descripcion
           }

def getProducto(id):
    descripcionDefault = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

    productos = (('Soporte Individual', 300, 5, 'soporte-bg.png', descripcionDefault),
                 ('Pack Strainer x3 ', 850, 4, 'pack-bg.png', descripcionDefault),
                 ('Pack Strainer x6', 1650, 4, 'pack2.png', descripcionDefault),
                 ('Taza Strainer', 1700, 3, 'taza2.png', descripcionDefault),
                 ('Cafetera Dolce Gusto', 24000,  1, 'cafetera-dolce.webp', descripcionDefault),
                 ('Cafetera Oyster', 39000,  1, 'cafetera-oster.webp', descripcionDefault),
                 ('Cápsulas Dolce Gusto Chococino', 2700, 2, 'capsulas-chococino.webp', descripcionDefault),
                 ('Cápsulas Dolce Gusto Lungo', 2700, 2, 'capsulas-lungo.webp', descripcionDefault),
                 ('Cápsulas Dolce Gusto Café con Leche', 2700, 2, 'capsulas-cafeconleche.webp', descripcionDefault),
                 ('Remera Vaso', 2700, 3, 'remera-vaso.webp', descripcionDefault),
                 ('Remera Astronauta Luna', 2700, 3, 'remera-astronauta-luna.webp', descripcionDefault),
                 ('Remera Astronauta Taza', 2700, 3, 'remera-astronauta-cafe.webp', descripcionDefault),
                 ('Remera Casa Cafetera', 2700, 3, 'remera-casa.webp', descripcionDefault))

    if (id > 0) and (id <= len(productos)):
        return tuple((id, productos[id-1][0], productos[id-1][1], productos[id-1][2], productos[id-1][3], productos[id-1][4]))
    else:
        return "*** ERROR ***"
