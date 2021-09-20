import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { Container, Card } from 'react-bootstrap';
import WeatherForcasts from './components/WeatherForcasts';
function App() {
  const [forcasts, setForcasts] = useState([])
  const testList = [
    {
      "id": 1,
      temp: "70 F"
    },
    {
      id: 2,
      temp: "32 F"
    },
    {
      id: 3,
      temp: "75 F"
    },
  ]
  return (
    <div className="App">
      <WeatherForcasts forcasts={testList}/>
    </div>
  );
}

export default App;
