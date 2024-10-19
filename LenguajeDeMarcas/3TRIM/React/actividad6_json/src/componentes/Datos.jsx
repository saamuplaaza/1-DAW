import "../hojas_de_estilo/Datos.css";

const Datos = ({nombre, apellidos, puesto, correo}) => {
    return(
        <div className="datos">
            <img src="https://picsum.photos/200" alt="imagen" />
            <h2>{apellidos}, {nombre}</h2>
            <div>
                <p>{puesto}</p>
                <p>{correo}</p>
            </div>
        </div>
    )
};

export {Datos};