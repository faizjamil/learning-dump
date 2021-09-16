import PropTypes from 'prop-types'

const header = ({title}) => {
  return (
    <header>
      <h1>{title}</h1>
    </header>
  )
}

header.defaultProps = {
  title: 'Test defaults',

}
header.propTypes = {
  title: PropTypes.string
}
export default header
