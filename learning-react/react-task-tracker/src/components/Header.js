import PropTypes from 'prop-types'
import { useLocation } from 'react-router'
import Button from './Button'

const Header = ({title, onAdd, showAdd}) => {
  const location = useLocation()
  return (
    <header className='header'>
      <h1>{title}</h1>
      {location.pathname === '/' &&<Button color={showAdd ? 'red' : 'green'} text={showAdd ? 'Close' : 'Add'} onClick={onAdd}/>}
    </header>
  )
}

Header.defaultProps = {
  title: 'Test defaults',
  showAdd: false
}
Header.propTypes = {
  title: PropTypes.string
}

// CSS in javascript
// const headingStyle = {
//   color: 'red',
//   backgroundColor: 'black'
// }
export default Header
