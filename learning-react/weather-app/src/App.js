import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { Container, Card } from 'react-bootstrap';

function App() {
  const [forcasts, setForcasts] = useState([])
  const testlist = [
    {
      id: 1,
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
      
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
