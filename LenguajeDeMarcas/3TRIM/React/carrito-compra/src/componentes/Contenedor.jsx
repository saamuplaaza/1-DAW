import "../hojas_de_estilo/Contenedor.css";
import "../hojas_de_estilo/CarritoCompra.css";
import { Datos } from "./Datos";
import { ProductosCarrito } from "./ProductosCarrito";
import data from "../Datos.json";
import { useState } from "react";
import { BiCheckCircle } from "react-icons/bi";

const Contenedor = () => {
    const [visible, setVisible] = useState(false);
    const [finalizado, setFinalizado] = useState(false);
    const [productos, setProductos] = useState([]);
    const [total, setTotal] = useState(0);
    const [cantidadProductos, setCantidadProductos] = useState(0);

    

    const agregarProducto = producto => {
        const productoExistente = productos.find(item => item.id === producto.id);
        if (productoExistente) {
            // Si el producto ya está en el carrito, aumentar la cantidad
            const carritoActualizado = productos.map(item =>
                item.id === producto.id ? { ...item, cantidad: item.cantidad + 1 } : item
            );
            setProductos(carritoActualizado)
            setTotal(total + (producto.precio-(producto.precio*producto.descuento)))
            setCantidadProductos(cantidadProductos +1)
            
        } else {
            // Si el producto no está en el carrito, agregarlo con cantidad 1
            const productoNuevo = { ...producto, cantidad: 1 };
            setProductos([...productos, productoNuevo]);
            setTotal(total + (producto.precio-(producto.precio*producto.descuento)))
            setCantidadProductos(cantidadProductos +1)
        }
    }

    const eliminarProducto = (id, precio, descuento, cantidad) => {
        const productosActualizados = productos.filter(producto => producto.id !== id);
        setProductos(productosActualizados);
        setTotal(total - ((precio-(precio*descuento))*cantidad));
        setCantidadProductos(cantidadProductos - cantidad);
    }

    const sumarProducto = (id, precio, descuento) => {
        const productosActualizados = productos.map(item => {
            if (item.id === id){
                const cantidadNueva = item.cantidad +1;
                return { ...item, cantidad: cantidadNueva };
            }
            return item; 
            }
        )
        const cantidadesActualizadas = productosActualizados.filter(item => item !== null);
        setProductos(cantidadesActualizadas);
        setTotal(total + (precio - (precio * descuento)));
        setCantidadProductos(cantidadProductos +1);
    }

    const restarProducto = (id, precio, descuento) => {
        const productosActualizados = productos.map(item => {
            if (item.id === id){
                const cantidadNueva = item.cantidad -1;
                if (cantidadNueva <= 0) {
                    // Si la nueva cantidad es cero o menor, eliminar el producto del carrito
                    return null; // Marcar el elemento para ser filtrado posteriormente
                } else {
                    return { ...item, cantidad: cantidadNueva };
                }
            }
            return item; 
            }
        )
        const cantidadesActualizadas = productosActualizados.filter(item => item !== null);
        setProductos(cantidadesActualizadas);
        setTotal(total - (precio - (precio * descuento))+1e-10);
        setCantidadProductos(cantidadProductos - 1);
    }


    const vaciarCarrito = () =>{
        setProductos([])
        setTotal(0)
        setCantidadProductos(0);
    }

    const cambiarVisible = () => {
        setVisible(!visible)
    }

    const cambiarFinalizado = () =>{
        setFinalizado(!finalizado)
        vaciarCarrito()
        setVisible(!visible)
    }

    const cerrarVentanaFinal = () =>{
        setFinalizado(!finalizado)
    }

    return(
        <>
            {/* Encabezado */}
            <div className="encabezado">
                <img src={require("../imagenes/logo_deza.png")} alt="Logo Deza"/>
                <h1>Deza Calidad</h1>  
                <button className="carrito" onClick={cambiarVisible}>
                    <img src={require("../imagenes/carrito.compra.png")} alt="Botón carrito compra" />
                    <p>{cantidadProductos}</p>
                </button>
            </div>
            {/* Contenedor */}
            <div className="contenedor">
            {data.map(producto => (
                <Datos
                    key = {producto.id}
                    id = {producto.id}
                    nombre={producto.nombre}
                    precio={producto.precio}
                    imagen={producto.imagen}
                    descuento={producto.descuento}
                    agregarProducto={agregarProducto}
                ></Datos>
            ))}
            </div>
            {visible ? <div className="oscurecer" onClick={cambiarVisible}></div> : <></>}
            
            {/* Carrito de la compra */}
            <div>
                <div className={visible? "productos-lista-contenedor visible" : "productos-lista-contenedor"}>
                    <div className="encabezado-carrito">
                        <button className="boton-cerrar-carrito" onClick={cambiarVisible}>X</button>
                        <img src={require("../imagenes/logo_deza.png")} alt="Logo Deza"/>
                        <button className="boton-vaciar-carrito" onClick={vaciarCarrito}><p>Eliminar todo</p> <img src={require("../imagenes/papelera.png")} alt="" /></button>
                    </div>
                    <div className="contenedor-productos-carrito">
                        {productos.map((item) => (
                            <ProductosCarrito
                                key = {item.id}
                                cantidad={item.cantidad}
                                nombre={item.nombre}
                                precio={item.precio}
                                descuento= {item.descuento}
                                imagen={item.imagen}
                                eliminarProducto={() => eliminarProducto(item.id, item.precio, item.descuento, item.cantidad)}
                                restarProducto={() => restarProducto(item.id, item.precio, item.descuento)}
                                agregarProducto={() => sumarProducto(item.id, item.precio, item.descuento)}
                            ></ProductosCarrito>
                        ))}
                    </div>
                    <div className={visible? "total-carrito visible" : "total-carrito"}>
                        <p className="total-carrito-parrafo">
                            Total: {total.toFixed(2)}€
                        </p>
                        <button className="boton-pagar-carrito" onClick={(cambiarFinalizado)}>Comprar</button>
                    </div>
                </div>
            </div>
            {finalizado ? <div className="oscurecer-todo" onClick={cerrarVentanaFinal}></div> : <></>}

            {finalizado ? <div className= "compra-finalizada visible">
                            <p><BiCheckCircle color="green" size={150}/></p>
                            <p>¡Gracias por la compra!</p>
            </div> : <></>}
                
        </>
    )
};

export {Contenedor};