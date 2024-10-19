import "../hojas_de_estilo/Datos.css";
import { BsHeartFill } from "react-icons/bs";
import { useState } from "react";


const Datos = ({id, nombre, precio, imagen, descuento, agregarProducto}) => {

const handleAgregar = () => {
    const producto = {
        id,
        nombre,
        precio,
        imagen,
        descuento
    };
    agregarProducto(producto)
}
const [visible, setVisible] = useState(false);

const cambiarVisible = () => {
    setVisible(!visible)
}

    if (descuento ===0 ){
        if(precio >= 1){
            return(
                <div className="datos">
                    {/* <button className="boton-me-gusta">Me gusta</button> */}
                    <button className={visible? "boton-me-gusta activo" : "boton-me-gusta"} onClick={cambiarVisible}><BsHeartFill size={20}/></button>
                    <div className="imagen">
                        <img className="imagenProducto" src={imagen} alt="imagen" />
                    </div>
                    <h2>{nombre}</h2>
                    <p className="precio">{precio.toFixed(2)}€</p>
                    <button className="boton-añadir" onClick={handleAgregar}>Añadir</button>
                </div>
            ); 
        } else{
            return(
                <div className="datos">
                    <button className={visible? "boton-me-gusta activo" : "boton-me-gusta"} onClick={cambiarVisible}><BsHeartFill size={20}/></button>
                    <div className="imagen">
                        <img className="imagenProducto" src={imagen} alt="imagen" />
                    </div>
                    <h2>{nombre}</h2>
                    <p className="precio">{(precio*100).toFixed(2)} cént</p>
                    <button className="boton-añadir" onClick={handleAgregar}>Añadir</button>
                </div>
            );
        }
    } else{
        if(precio >= 1){
            return(
                <div className="datos">
                    {/* <button className="boton-me-gusta">Me gusta</button> */}
                    <button className={visible? "boton-me-gusta activo" : "boton-me-gusta"} onClick={cambiarVisible}><BsHeartFill size={20}/></button>
                    <div className="imagen">
                        <img className="imagenProducto" src={imagen} alt="imagen" />
                    </div>
                    <h2>{nombre}</h2>
                    <p className="precio">{(precio - (precio*descuento)).toFixed(2)} €</p>
                    <p className="precioDescuento">{precio}€</p>
                    <button className="boton-añadir" onClick={handleAgregar}>Añadir</button>
                    <p className="descuento">-{descuento*100}%</p>
                    <img className="iconoDescuento" src={require("../imagenes/descuento.png")} alt="Descuento del producto" />
                </div>
            );
        } else{
            return(
                <div className="datos">
                    {/* <button className="boton-me-gusta">Me gusta</button> */}
                    <button className={visible? "boton-me-gusta activo" : "boton-me-gusta"} onClick={cambiarVisible}><BsHeartFill size={20}/></button>
                    <div className="imagen">
                        <img className="imagenProducto" src={imagen} alt="imagen" />
                    </div>
                    <h2>{nombre}</h2>
                    <p className="precio">{(precio - (precio*descuento)).toFixed(2)} €</p>
                    <p className="precioDescuento">{precio*100} cént</p>
                    <button className="boton-añadir" onClick={handleAgregar}>Añadir</button>
                    <p className="descuento">-{descuento*100}%</p>
                    <img className="iconoDescuento" src={require("../imagenes/descuento.png")} alt="Descuento del producto" />
                </div>
            );
        };
    }
};

export {Datos};