import { useState } from 'react';
import './App.css';
import {Dia} from "./componentes/Dia";
import data from "./Datos.json"
import { DiaSeleccionado } from './componentes/DiaSeleccionado';

function App() {

  const [diaSeleccionado, setDiaSeleccionado] = useState("");
  const [consultas, setConsultas] = useState({});


  const handleDia = (dia) => {
    setDiaSeleccionado(dia);
    setConsultas((prevConsultas) => ({
      ...prevConsultas,
      [dia.fecha]: (prevConsultas[dia.fecha] || 0) + 1,
    }));
  }

  return (
    <>
      <h1>El tiempo en Córdoba</h1>
      <>
        {diaSeleccionado ? (
          <>
            <div className="ppal">
              <DiaSeleccionado
                diasemana={diaSeleccionado.diasemana}
                fecha={diaSeleccionado.fecha}
                imagen={diaSeleccionado.imagen}
                tmax={diaSeleccionado.tmax}
                tmin={diaSeleccionado.tmin}
              />
            </div>
            <h2>Número de veces consultado el {diaSeleccionado.fecha}: {consultas[diaSeleccionado.fecha]}</h2>
          </>
        ) : (
          <p className='ppal'>Selecciona un día para ver el detalle</p>
        )}
      </>


      <div className="contenedor">
        {data.map(dia=>(
          <Dia
          key={dia.id}
          id = {dia.id}
          diasemana = {dia.diasemana}
          fecha = {dia.fecha}
          imagen = {dia.imagen}
          tmax = {dia.tmax}
          tmin = {dia.tmin}
          seleccionar = {() =>handleDia(dia)}
          ></Dia>
        ))}
      </div>
    </>
  );
}

export default App;
