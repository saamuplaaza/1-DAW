import React from "react";
import "../hojas_de_estilos/ListaDeTareas.css";
import TareaFormulario from "./TareaFormulario";
import Tarea from "./Tarea";
import { useState } from "react";

function ListaDeTareas(){
    const [tareas, setTareas] = useState([]);

    const agregarTarea = tarea => {
        const tareasActualizadas = [tarea, ...tareas];
        setTareas(tareasActualizadas);
      }
    
      const eliminarTarea = id => {
        const tareasActualizadas = tareas.filter(tarea => tarea.id !== id);
        setTareas(tareasActualizadas);
      }
    
      const completarTarea = id => {
        const tareasActualizadas = tareas.map(tarea => {
          if (tarea.id === id){
            tarea.completada = !tarea.completada;
          }
          return tarea;
        });
        setTareas(tareasActualizadas);
      }

    return(
        <>
            <TareaFormulario onSubmit = {agregarTarea}/>
            <div className="tareas-lista-contenedor">
                {tareas.map((tarea) => 
                    <Tarea 
                        key={tarea.id}
                        id={tarea.id}
                        texto={tarea.texto}
                        completada={tarea.completada}
                        completarTarea={completarTarea}
                        eliminarTarea={eliminarTarea}
                    ></Tarea>)
                }
            </div>
        </>
    )
}

export default ListaDeTareas;