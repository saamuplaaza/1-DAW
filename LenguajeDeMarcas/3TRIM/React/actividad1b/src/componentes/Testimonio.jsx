import React from "react";
import "../hojas_de_estilo/testimonio.css";

function Testimonio(props){
    return(
        <div className="contenedor-testimonio">
            <div className="contenedor-texto-testimonio">
                <h3 className="nombre-testimonio">{props.nombre} en {props.ciudad}</h3>
                <p className="texto-testimonio">{props.testimonio}</p>
                <a href={props.enlace}>Página oficial de {props.nombre2}</a>
            </div>
            <img src={require(`../imagenes/${props.imagen}.jpg`)} alt={`Foto de ${props.nombre}`} className="imagen-testimonio" />
        </div>
    )
}

export default Testimonio