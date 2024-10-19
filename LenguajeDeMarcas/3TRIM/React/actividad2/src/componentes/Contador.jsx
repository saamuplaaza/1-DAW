import React from "react";
import "../hojas_de_estilo/Contador.css"

function Contador({numClics}){
    return(
        <div className="contador">
            {numClics}
        </div>
    );
}

export default Contador