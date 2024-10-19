import "../hojas_de_estilo/Contenedor.css";

const Contenedor = (props) => {
    return(
        <div className="contenedor">
            {props.children}
        </div>
    )
};

export {Contenedor};