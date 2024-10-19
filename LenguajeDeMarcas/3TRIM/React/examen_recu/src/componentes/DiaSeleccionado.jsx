import React from "react";

const DiaSeleccionado = (props) =>{
    return(
        <div>
            <h2>{props.diasemana}, {props.fecha}</h2>
            <img className="imagen" src={require(`../imagenes/${props.imagen}`)} alt="imagen" />
            <h3>min. {props.tmin} - max. {props.tmax}</h3>
        </div>
    )
}

export {DiaSeleccionado}