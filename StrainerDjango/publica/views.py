from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):    
    return render(request, 'publica/index.html')

def origenes(request):    
    return render(request, 'publica/origenes.html')

def tienda(request):    
    return render(request, 'publica/tienda.html', getContextoTienda())

def getContextoTienda():
    return {
        "categorias": getDictCategorias(),
        "productos": getDictProductos(),
    } 

#########################################################################
#                                                                       #
# Cuando agreguemos la Base de Datos las siguientes funciones vuelan... #
#                                                                       #
#########################################################################

def getDictCategorias():
    selectDistinctCategoriasFromProductos = []
    for n in range(1, 6):
        selectDistinctCategoriasFromProductos.append(getDictCategoria(n))
    return selectDistinctCategoriasFromProductos

def getDictCategoria(id):
    return {"id": id, "categoria": getCategoria(id)}

def getCategoria(id):
    categorias = ("Cafeteras", "Cápsulas", "Merchandising", "Packs", "Soportes")
    if (id > 0) and (id <= len(categorias)):
        return categorias[id-1]
    else:
        return "*** ERROR ***"

def getDictProductos():

    descripcionDefault = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

    selectProductosFromProductosYCategorias = []
    selectProductosFromProductosYCategorias.append(getDictProducto(1, 'Soporte Individual', 300, 5, 'soporte-bg.png', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(2, 'Soporte Individual', 300, 5, 'soporte-bg.png', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(3, 'Pack Strainer x3 ', 850, 4, 'pack-bg.png', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(4, 'Pack Strainer x6', 1650, 4, 'pack2.png', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(5, 'Taza Strainer', 1700, 3, 'taza2.png', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(6, 'Cafetera Dolce Gusto', 24000,  1, 'cafetera-dolce.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(7, 'Cafetera Oyster', 39000,  1, 'cafetera-oster.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(8, 'Cápsulas Dolce Gusto Chococino', 2700, 2, 'capsulas-chococino.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(9, 'Cápsulas Dolce Gusto Lungo', 2700, 2, 'capsulas-lungo.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(10, 'Cápsulas Dolce Gusto Café con Leche', 2700, 2, 'capsulas-cafeconleche.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(11, 'Remera Vaso', 2700, 3, 'remera-vaso.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(12, 'Remera Astronauta Luna', 2700, 3, 'remera-astronauta-luna.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(13, 'Remera Astronauta Taza', 2700, 3, 'remera-astronauta-cafe.webp', descripcionDefault))
    selectProductosFromProductosYCategorias.append(getDictProducto(14, 'Remera Casa Cafetera', 2700, 3, 'remera-casa.webp', descripcionDefault))
    return selectProductosFromProductosYCategorias

def getDictProducto(id, nombre, precio, id_categoria, imagen, descripcion):
    return {
            "id": id,
            "nombre": nombre,
            "precio": precio, 
            "id_categoria": id_categoria, 
            "categoria": getCategoria(id_categoria), 
            "imagen": imagen, 
            "descripcion": descripcion
           }
