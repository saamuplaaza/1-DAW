import React from "react";
import "../hojas_de_estilo/Boton.css";

function Boton({texto, esBotonDeClick, manejarClic}) {
    return(
        <button 
            className= {esBotonDeClick ? "boton-clic" : "boton-reiniciar"}
            onClick={manejarClic}
            >{texto}</button>
    );
}

export default Boton;