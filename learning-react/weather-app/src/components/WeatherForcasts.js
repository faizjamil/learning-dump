import React from 'react'
import WeatherForcast from './WeatherForcast'
const WeatherForcasts = ({forcasts}) => {
  return (
    <div className='container'>
        {forcasts.map((forcast) => (
          <div className='row'>
            <WeatherForcast key={forcast.id} forcast={forcast} />
          </div>
        ))}
      
  
    
        
      
    </div>
  )
}

export default WeatherForcasts
