import './App.css';
import {Contenedor} from './componentes/Contenedor';
import {Datos} from "./componentes/Datos" 
import data from "./Datos.json"

function App() {
  return (
    <div className="App">
      <Contenedor>
        {data.map(datos =>
          <Datos
            id = {datos.id}
            nombre={datos.nombre}
            apellidos={datos.apellidos}
            puesto={datos.puesto}
            correo={datos.correo}
          ></Datos>
        )}
      </Contenedor>
    </div>
  );
}

export {App};
