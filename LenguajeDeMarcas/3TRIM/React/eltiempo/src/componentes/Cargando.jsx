import styles from '../hojas-de-estilo/Loading.css';

export default function Cargando() {
  return (
    <div className={styles.loadingContainer}>
      <div className={styles.loader}>
        <div></div>
      </div>
    </div>
  );
}