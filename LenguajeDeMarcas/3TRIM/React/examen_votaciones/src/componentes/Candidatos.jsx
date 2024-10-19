import React from "react";
import "../index.css"

const Candidatos = (nombre, grupo, imagen, sumarVoto, votos)=>{
    return(
        <div className="candidato">
            <p>{nombre}</p>
            <p className="menu">{grupo}</p>
            {/* <img src={require(imagen)} alt="imagen del candidato"></img> */}
            <button className="cajaVotacion" onClick={sumarVoto}>Vótame</button>
            <div className="votacion">{votos}</div>
        </div>
    );
};
export {Candidatos};