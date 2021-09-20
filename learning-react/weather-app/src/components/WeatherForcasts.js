import React from 'react'
import WeatherForcast from './WeatherForcast'
const WeatherForcasts = (forcasts) => {
  return (
    <>
      {forcasts.map((forcast) => (
        <WeatherForcast key={forcast.id} forcast={forcast} />
      ))}
    </>
  )
}

export default WeatherForcasts
