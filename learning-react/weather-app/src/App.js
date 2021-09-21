import './App.css';
import { useState } from 'react';
import WeatherForcasts from './components/WeatherForcasts';
function App() {
  const [forcasts, setForcasts] = useState([])
  const [darkMode, setDarkMode] = useState(false)
  const testList = [
    {
      id: 1,
      currentTemp: "70 F",
      lowTemp: "66 F",
      highTemp: "81 F"
    },
    {
      id: 2,
      currentTemp: "32 F",
      lowTemp: "30 F",
      highTemp: "36 F"
    },
    {
      id: 3,
      currentTemp: "75 F",
      lowTemp: "72 F",
      highTemp: "79 F"
    },
  ]
  return (
    
    
    <div className='App' >
      {
        testList.length > 0 && <WeatherForcasts forcasts={testList}/>
        
      }

      <input onChange={() => setDarkMode(!darkMode) }type='checkbox' id='dark-mode' name='dark-mode' value='Dark Mode' />
      <label style={{ paddingLeft: '0.25rem'}}for='dark-mode'>Dark Mode</label>
        
      
    </div>
  );
}




export default App;
