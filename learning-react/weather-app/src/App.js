import './App.css';
import {ThemeProvider} from "styled-components";
import { GlobalStyles } from "./components/globalStyles";

import { lightTheme, darkTheme } from "./components/Themes"

import { useState, useEffect } from 'react';
import WeatherForcasts from './components/WeatherForcasts';
function App() {
  const [forcasts, setForcasts] = useState([])
  const [darkMode, setDarkMode] = useState(true)
  const [theme, setTheme] = useState('light');
  useEffect(() => {
    const getForcasts = async () => {
      const forcastsFromServer = await fetchForcasts()
      setForcasts(forcastsFromServer)
    }
    getForcasts()

  })
  
  
  const themeToggler = () => {
    theme === 'light' ? setTheme('dark') : setTheme('light')
  }
  


  const fetchForcasts = async () => {

    const res = await fetch('http://localhost:5000/forcasts')
    const data = res.json()
    return data
  }
  const fetchForcast = async (id) => {

    const res = await fetch(`http://localhost:5000/forcasts/${id}`)
    const data = res.json()
    return data
  }
  // const forcasts = [
  //   {
  //     id: 1,
  //     currentTemp: "70 F",
  //     lowTemp: "66 F",
  //     highTemp: "81 F"
  //   },
  //   {
  //     id: 2,
  //     currentTemp: "32 F",
  //     lowTemp: "30 F",
  //     highTemp: "36 F"
  //   },
  //   {
  //     id: 3,
  //     currentTemp: "75 F",
  //     lowTemp: "72 F",
  //     highTemp: "79 F"
  //   },
  // ]
  return (
    
    <ThemeProvider theme={theme === 'light' ? lightTheme : darkTheme}>
      <>
        <GlobalStyles/>
        <div className='App' >
          <button onClick={themeToggler}>Switch Theme</button>
            {
              forcasts.length > 0 &&  <WeatherForcasts forcasts={forcasts}/>
            }
        </div>
      </>
    </ThemeProvider>
  );
}




export default App;
