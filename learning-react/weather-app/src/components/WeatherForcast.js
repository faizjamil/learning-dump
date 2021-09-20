import React from 'react'
import { Col, Card } from 'react-bootstrap'
import {FaSun} from 'react-icons/fa'
const WeatherForcast = ({ forcast }) => {
  return (
    
    <Col>
      {forcast.temp}
      <FaSun />
    </Col>
  )
}

export default WeatherForcast
