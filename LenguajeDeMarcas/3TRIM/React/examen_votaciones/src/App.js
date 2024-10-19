import React from "react";
import { useState } from "react";
import data from "./Datos.json";
import {Candidatos} from "./componentes/Candidatos"


function App() {
  const [votos, setVotos] = useState(0)

  const sumarVoto = () => {
    setVotos(votos + 1)
  }


  return (
    <>
      <h1>Has votado a {} que obtiene un total de {}votos</h1>
      <div className="contenedor">
        {data.map(candidato=>(
          <Candidatos
            nombre = {candidato.nombre}
            grupo = {candidato.grupo}
            imagen = {candidato.imagen}
            sumarVoto = {sumarVoto}
            votos = {votos}/>
        ))}
      </div>
    </>
  );
}

export default App;
