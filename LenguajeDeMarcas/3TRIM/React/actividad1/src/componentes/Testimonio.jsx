import React from "react";
import "../hojas_de_estilos/Testimonio.css";

function Testimonio(props){
    return(
        <div className="contenedor-testimonio">
            <img className="imagen-testimonio" src={require(`../imagenes/${props.imagen}.png`)} alt={`Foto de ${props.nombre}`}></img>
            <div className="contenedor-texto-testimonio">
                <p className="nombre-testimonio"><strong>{props.nombre}</strong> en {props.pais}</p>
                <p className="cargo-testimonio">{props.nombre} en <strong>{props.empresa}</strong></p>
                <p className="testo-testimonio">{props.testimonio}</p>
            </div>
        </div>
    );
    
}

export default Testimonio;