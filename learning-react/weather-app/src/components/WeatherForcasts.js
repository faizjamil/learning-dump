import React from 'react'
import WeatherForcast from './WeatherForcast'
const WeatherForcasts = ({forcasts, darkMode}) => {
  return (
    <>
      {forcasts.map((forcast) => (
        <div className='row'>
          <WeatherForcast key={forcast.id} forcast={forcast} />
        </div>
      ))}
      
  
    
        
      
    </>
  )
}

export default WeatherForcasts
