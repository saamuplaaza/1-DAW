import React from "react";

const Dia = (props) => {
    return (
        <div className="dia">
            <h1>{props.diasemana}</h1>
            <img src={require(`../imagenes/${props.imagen}`)} alt="imagen" />
            <p>{props.tmax}</p>
            <button className="boton" onClick={props.seleccionar}>+ info</button>
        </div>
    )
}

export {Dia}