import React, { useState } from "react";

const Candidato = (props, imagen)=>{
    const [votos, setVotos] = useState(0);

    const handleVotar = () =>{
        setVotos(votos + 1)
        props.onVotar(props.nombre, props.votos + 1)
    }
    return(
        <div className="candidato">
            <h1>{props.nombre}</h1>
            <p className="menu">Grupo: {props.grupo} I.E.S. Fidiana</p>
            <img src={require(`../imagenes/${props.imagen}`)} alt="imagen del candidato"/>
            <div className="cajaVotacion">
                <button className="" onClick={handleVotar}>Vótame</button>
                <div className="votacion">{votos}</div>
            </div>
        </div>
    )
}
export {Candidato};
