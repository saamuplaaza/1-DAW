import './App.css';
import { useState } from 'react';
import Contador from './componentes/Contador';
import Boton from './componentes/Boton';

function App() {

  // const [stateLuz, setStateLuz] = useState(false);

  // const encenderApagar = () =>{
  //   setStateLuz(!stateLuz)
  // }

  const [numClics, setStateNumero] = useState(0)

  const aumentarContador = () =>{
    setStateNumero(numClics+ 1)
  }

  const reiniciarContador = () =>{
    setStateNumero(0)
  }

  return (
    <div className="App">
      <header className="contenedor-principal">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <h3>La luz está: {stateLuz ? "Encendida" : "Apagada"}</h3>
        <button onClick={encenderApagar}>Encender / Apagar</button> */}
        <Contador numClics = {numClics}></Contador>
        <Boton 
          texto = "Click"
          esBotonDeClick = {true}
          manejarClic = {aumentarContador}>
        </Boton>
        <Boton
          texto = "Reiniciar"
          esBotonDeClick = {false}
          manejarClic = {reiniciarContador}>
        </Boton>
      </header>
    </div>
  );
}

export default App;
