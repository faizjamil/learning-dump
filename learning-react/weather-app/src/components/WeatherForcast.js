import { useState } from 'react'
import React from 'react'
import {FaSun} from 'react-icons/fa'
const WeatherForcast = ({ forcast, darkMode }) => {
  const [isCollapsed, setIsCollapsed] = useState(true)
  return (
    
    <div className='container'>
      
      
      <h5 className='card-title'>{forcast.currentTemp}
        <FaSun style={forcastStyle} alt='Sunny' />
      </h5>

      High: {forcast.highTemp}
      
      <br/>
      
        Low: {forcast.lowTemp}      
      
      <br/>
      
      <br/>
      <button style={buttonStyle} className='btn btn-primary mx-auto' type='button' 
      onClick={() =>setIsCollapsed(!isCollapsed)}>Details</button>
      <br/>
      {!isCollapsed &&

        <p>
          Details go here
        </p>
      }
      
    </div>
  )
}

const forcastStyle = {
  paddingLeft: 5, 
  paddingBottom: 5,
  // apply this style only when dark mode is enabled
  // filter: 'invert(100%)',
}
const buttonStyle = {
  paddingTop: 3,
  width: '5rem',
  display: 'block'
}

export default WeatherForcast
