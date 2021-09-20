import React from 'react'
import { Card } from 'react-bootstrap'

const WeatherForcast = ({ forcast }) => {
  return (
    <Card>
      {forcast.temp}
    </Card>
  )
}

export default WeatherForcast
