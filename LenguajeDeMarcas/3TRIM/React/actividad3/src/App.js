import './App.css';
import  Pantalla from "./componentes/Pantalla";
import Boton from "./componentes/Boton";
import BotonClear from "./componentes/BotonClear";
import { useState } from 'react';

function App() {

  const[input, setInput] = useState("");

  const agregarInput = val =>{
    setInput(input+val)
  };

  const calcularResultado = () => {
    setInput(eval(input));
    
  };

  return (
    <div className="App">
      <header className='contenedor-calculadora'>
        <Pantalla input = {input}/>
        <div className='fila'>
          <Boton manejarClick = {agregarInput}>1</Boton>
          <Boton manejarClick = {agregarInput}>2</Boton>
          <Boton manejarClick = {agregarInput}>3</Boton>
          <Boton manejarClick = {agregarInput}>+</Boton>
        </div>
        <div className='fila'>
          <Boton manejarClick = {agregarInput}>4</Boton>
          <Boton manejarClick = {agregarInput}>5</Boton>
          <Boton manejarClick = {agregarInput}>6</Boton>
          <Boton manejarClick = {agregarInput}>-</Boton>
        </div> 
        <div className='fila'>
          <Boton manejarClick = {agregarInput}>7</Boton>
          <Boton manejarClick = {agregarInput}>8</Boton>
          <Boton manejarClick = {agregarInput}>9</Boton>
          <Boton manejarClick = {agregarInput}>*</Boton>
        </div> 
        <div className='fila'>
          <Boton manejarClick = {calcularResultado}>=</Boton>
          <Boton manejarClick = {agregarInput}>0</Boton>
          <Boton manejarClick = {agregarInput}>.</Boton>
          <Boton manejarClick = {agregarInput}>/</Boton>
        </div> 
        <div className='fila'>
          <BotonClear manejarClear = {()=> setInput('')}>Clear</BotonClear>
        </div> 
      </header>
    </div>
  );
}

export default App;
