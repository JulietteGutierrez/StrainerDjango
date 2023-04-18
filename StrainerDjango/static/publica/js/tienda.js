import productos from './productos.js'

        /****** Dibujar productos ******/

        const formatoPrecio = precio => precio.toLocaleString('de-DE', { minimumFractionDigits: 2 , maximumFractionDigits: 2})

        function dibujarProductos(productos){
            let listadoProductos = ''
            for(let i=1; i<=productos.length; i++){
                const producto = productos[i-1]
                listadoProductos += `
                    <article id="producto${i}" class="producto">
                        <div class="box-img">
                            <img class="producto--img" src="../assets/img/productos/${producto.imagen}">
                        </div>
                        <div class="producto--datos">
                            <h3 class="producto--nombre">${producto.nombre}</h3>
                            <p>$${formatoPrecio(producto.precio)}</p>
                        </div>
                    </article>
                `
            }

            document.getElementById('contenedor-productos').innerHTML=(listadoProductos)
        }

        /****** Filtros ******/

        function aplicarFiltros(){
            dibujarProductos(
                filtrarPorCategoria(
                    filtrarPorNombre(productos, filtro_nombre.value??".*")
                    , filtro_categoria.value
                )
            )
        }

        function filtrarPorNombre(productos, nombre){
            const regex = new RegExp(".*"+nombre.toLowerCase() + ".*")
            return nombre == ''? productos: productos.filter(p=>regex.test(p.nombre.toLowerCase()))
        }

        function filtrarPorCategoria(productos, categoria){
            const CUALQUIERA = 'Todas'
            return categoria===CUALQUIERA? productos: productos.filter(p=>p.categorias.includes(categoria))
        }

        /****** Inicializar ******/

        dibujarProductos(productos)

        function cargarCategorias(){
            let opciones = ''
            const categorias = productos.flatMap(p=>p.categorias)
            new Set(categorias).forEach(categoria=>{
                opciones+= `
                    <option value="${categoria}">${categoria}</option>
                `
            })

            filtro_categoria.innerHTML+=opciones
        }

        [filtro_nombre, filtro_categoria].forEach(f=>f.addEventListener('input',ev => aplicarFiltros()))

        cargarCategorias()