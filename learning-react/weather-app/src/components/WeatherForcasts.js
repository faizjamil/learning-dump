import React from 'react'
import { Row, Col, Container } from 'react-bootstrap'
import WeatherForcast from './WeatherForcast'
const WeatherForcasts = ({forcasts}) => {
  return (
    <div>
    
      <Container >
        <Row xs={2} md={4} lg={6}>
          {forcasts.map((forcast) => (
            <Col xs={6} md={4}>
              <WeatherForcast key={forcast.id} forcast={forcast} />
            </Col>
          ))}
        
        </Row>
      </Container>
      
    </div>
  )
}

export default WeatherForcasts
