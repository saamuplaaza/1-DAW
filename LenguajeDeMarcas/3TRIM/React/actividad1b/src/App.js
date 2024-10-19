import './App.css';
import Testimonio from './componentes/Testimonio';


function App() {
  return (
    <div className="App">
      <div className='contenedor-principal'>
        <h1>Página de viajes de Samuel</h1>
        <h2>En esta página vamos a hablar de lugares fantásticos para visitar en la estación de primavera para las personas con alergia al polen.</h2>
        <Testimonio
        imagen = "parisMediano"
        nombre = "La Torre Eiffel"
        nombre2 = "la Torre Eiffel"
        ciudad = "París"
        testimonio = "Venga a descubrir la Torre Eiffel en un viaje ascendente único en el mundo y déjese llevar por las emociones que vivirá en su ascenso desde el atrio hasta la cima."
        enlace = "https://www.toureiffel.paris/es"
        >
        </Testimonio>
        <Testimonio
        imagen = "La fiesta de las Luces-Mediano"
        nombre = "La fiesta de las Luces"
        nombre2 = "La Fiesta de las Luces"
        ciudad = "Lyon"
        testimonio = "Esta fiesta religiosa conmemora a la Virgen María, que, según los dichos, llevó la luz a los habitantes de Lyon durante los días oscuros de la peste, permitiendo que la ciudad se salvara. Hoy, la fiesta se celebra encendiendo velas e iluminando las calles de Lyon."
        enlace = "https://latiendafrancesa.mx/la-fiesta-de-las-luces/#:~:text=Esta%20fiesta%20religiosa%20conmemora%20a,iluminando%20las%20calles%20de%20Lyon"
        ></Testimonio>
        <Testimonio
        imagen = "El Carnaval de Niza-Mediano"
        nombre = "El Carnaval de Niza"
        nombre2 = "El Carnaval de Niza"
        ciudad = "Niza"
        testimonio = "A lo largo de 15 días, la ciudad de Niza vive al ritmo de uno de los acontecimientos más importantes del sur de Francia, favorecida por el clima benigno de la región de la Costa Azul, con un invierno luminoso, a menudo soleado y con temperaturas suaves."
        enlace = "https://www.la-provenza.es/carnaval-de-niza"
        ></Testimonio>
      </div>
    </div>
  );
}

export default App;
