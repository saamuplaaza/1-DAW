import './App.css';
import Testimonio from "./componentes/Testimonio";

function App() {
  return (
    <div className="App">
      <div className='contenedor-principal'>
        <h1>Esto es lo que opinan nuestros alumnos sobre freecodecamp:</h1>
        <Testimonio
          imagen = "Shawn"
          nombre = "Shawn Wang"
          pais = "Singapur"
          cargo = "Ingeniero de Software"
          empresa = "Amazon"
          testimonio = '"Da miedo cambiar de carrera. Solo gané la confianza de que podía programar trabajando a través de los cientos de horas de lecciones gratuitas en freeCodeCamp. Dentro de un año tuve un trabajo de seis cifras como ingeniero de software. freeCodeCamp cambió mi vida."'>
        </Testimonio>
        <Testimonio
          imagen = "Sarah"
          nombre = "Sarah Chima "
          pais = "Nigeria"
          cargo = "Ingeniera de Software"
          empresa = "ChatDesk"
          testimonio = '"freeCodeCamp fue la puerta de entrada a mi carrera como desarrollador de software. El plan de estudios bien estructurado llevó mis conocimientos de programación de un nivel de principiante total a un nivel muy seguro. Era todo lo que necesitaba para conseguir mi primer trabajo de desarrollador en una empresa increíble."'>
        </Testimonio>
        <Testimonio
          imagen = "Emma"
          nombre = "Emma Bostian "
          pais = "Nigeria"
          cargo = "Ingeniera de Software"
          empresa = "Spotify"
          testimonio = '"Siempre he tenido problemas para aprender JavaScript. He tomado muchos cursos, pero el curso de freeCodeCamp fue el que se quedó. Estudiar JavaScript, así como estructuras de datos y algoritmos en freeCodeCamp me dio las habilidades y la confianza que necesitaba para conseguir el trabajo de mis sueños como ingeniero de software en Spotify."'>
        </Testimonio>
      </div>
    </div>
  );
}

export default App;
