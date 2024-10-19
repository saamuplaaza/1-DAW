import { useState } from "react";
import data from "./Datos.json";
import {Candidato} from "./componentes/Candidato"


function App() {
  const [candidatoVotado, setCandidatoVotado] = useState("");
  const [votosCandidato, setVotosCandidato] = useState(0);


  const handleVotar = (nombre, votos) => {
    setCandidatoVotado(nombre);
    setVotosCandidato(votos)
  }

  return (
    <>
      <h1>Has votado a <span className="rojo">{candidatoVotado}</span> que obtiene un total de <span className="rojo">{votosCandidato}</span> votos</h1>
      <div className="contenedor">
        {data.map(candidato=>(
          <Candidato
            key = {candidato.id}
            id = {candidato.id}
            nombre = {candidato.nombre}
            grupo = {candidato.grupo}
            imagen = {candidato.imagen}
            onVotar = {handleVotar}
            votos = {candidato.votos}
            >
          </Candidato>
        ))}
      </div>
    </>
  );
}

export default App;

