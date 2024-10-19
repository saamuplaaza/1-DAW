import "../hojas_de_estilo/ProductosCarrito.css"


const ProductosCarrito = ({cantidad, nombre, precio, descuento, imagen, eliminarProducto, agregarProducto, restarProducto}) => {
    return (
        <div className="producto-carrito">
            <p className="cantidad">{cantidad}</p>
            <div className="imagen-prod-carrito">
                <img src={imagen} alt="imagen del producto"/>
            </div>
            <p className="producto-carrito-nombre">{nombre}</p>
            <p className="producto-carrito-precio">{((precio-(precio*descuento)) * cantidad).toFixed(2)} €</p>
            <div>
                <button className="boton sumar" onClick={agregarProducto}>+</button>
                <button className="boton restar" onClick={restarProducto}>-</button>
                <button className="boton papelera" onClick={eliminarProducto}>
                    <img src={require("../imagenes/papelera.png")} alt="papelera" />
                </button>
            </div>
        </div>
    )
};

export {ProductosCarrito};