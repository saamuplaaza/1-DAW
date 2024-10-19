import React from "react";
import "../hojas_de_estilos/Boton.css"

function esNumero(props){
    if (Number.parseInt(props.children) || props.children ==="0" || props.children ==="=" || props.children ===".") {
        return true
    }
    else{
        return false
    }
}

function Boton(props){
    if(esNumero(props) === true){
        return(
            <div className="boton-contenedor" onClick={() => props.manejarClick(props.children)}>
                {props.children}
            </div>
        )
    }
    else{
        return(
            <div className="boton-contenedor operador" onClick={() => props.manejarClick(props.children)}>
                {props.children}
            </div>
        )
    };
};

export default Boton;