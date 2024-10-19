import { useState, useEffect } from "react";
import Cargando from "./Cargando";
import WeatherForm from "./WeatherForm";
import WeatherMainInfo from "./WeatherMainInfo";
import '../hojas-de-estilo/WeatherApp.css'

import styles from "../hojas-de-estilo/WeatherApp.css";

export default function WeatherApp() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    loadInfo();
  }, []);
 
  useEffect(() => {
    document.title = "Weather | " + weather?.location?.name ?? "";
  }, [weather]);

  async function loadInfo(city = "london") {
    console.log(
      `${process.env.REACT_APP_URL}key=${process.env.REACT_APP_KEY}&q=${city}`
    );
    try {
      const request = await fetch(
        `${process.env.REACT_APP_URL}key=${process.env.REACT_APP_KEY}&q=${city}`
      );
      const json = await request.json();
      console.log(json);

      setTimeout(() => {
        setWeather({ ...json });
      }, 2000);
    } catch (e) {
      console.error(e);
    }
  }

  function handleOnChangeCity(city) {
    setWeather(null);
    loadInfo(city);
  }

  return (
    <div className={styles.weatherContainer}>
      <WeatherForm onChangeCity={handleOnChangeCity} />
      {weather ? <WeatherMainInfo weather={weather} /> : <Cargando />}
    </div>
  );
}