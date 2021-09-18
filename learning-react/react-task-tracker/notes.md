# What is React?

These notes are from [Traversy Media's 2021 React Crash Course](https://youtu.be/w7ejDZ8SWv8)

A library for building UIs.

It is considered a framework since it is capable of adding pieces from the React ecosystem to be comparable to the functionality of Angular and Vue.
Used with other technologies to create a full stack app.
MERN (MongoDB, Express.js, React, and Node.js) stack.
 
React runs as a Single Page Application

# Why React?

* Structure the view layer of your app
* Reuseable components with their own state
* JSX - Dynamic markup
* Interactive UIs with virtual DOM
* Performance and testing
* Popular in industry

# What you should know first

JavaScript 

* Data types, vars, funcitons, loops, etc.
* Promises and async programming
* Array methods like forEach and Map()
* Fetch API and making HTTP requests

# UI Components
Think of your UI as separate components when using React


# Components: Functions vs classes
Components render/return JSX
Components can also take in "props" (properties)

# Working with state

Components can have "state" which is an object that determines how a component renders and behaves.

"App" or "Global" state refers to state that is available to the entire UI, not just a single component.

Prior to React 16.8, had to use class based components to use state. 
Now we can use funcitonal components with **hooks**


# React Hooks
Functions that allow us to let us hook into the React state and lifecycle features from function components.

Examples:
* useState - Returns a stateful value and a function to update it
* useEffect - Perform side effects in function components
* useContent, useReducer, useRef, etc.

# Uncategorized notes
You can only return one parent element in App.js since JSX expressions must have one parent element.

WHen compiled, the following JSX returns a `<div>` with an id of `root` which then wraps around the following

```jsx
    <div className="App">
      <h1>Hello From React</h1>
    </div>
```
If you do not want the `h1` to be wrapped in a `div`, simply make the div a fragment by changing the `<dic>` to `<>`

The root `div` wraps around everything

You can pass a property (or prop) to any components you define in JSX

For example if we add a `<Header />` component in App.js, we can pass certain properties such as `title`

```jsx 
<Header title='Hello'/>
```

However right now this doesn't do anything since we need to handle that in the `Header` component

How do we do this?
Take the following component as an example
```jsx

const header = () => {
  return (
    <header>
      <h1>Task tracker</h1>
    </header>
  )
}

export default header
```

We pass `props` in as a parameter of the arrow function shown here. To use the `title` prob we defined earlier, we can use curly braces inside of the `h1` to access the `title`
```jsx
const header = (props) => {
  return (
    <header>
      <h1>{props.title}</h1>
    </header>
  )
}
export default header
```

We can also define default values for props, erase the `title` attribute from the `<Header />` tag in App.js and add the following below the return but above the export statement in Header.js
```jsx


header.defaultProps = {
  title: 'Test defaults',

}
```

To make the code in Header.js look a little cleaner, instead of passing the `props` object as a parameter we can use destructuring to get just the props we need, in this case title

Here's what Header.js looks like when we use destructuring.
```jsx
const header = ({title}) => {
  return (
    <header>
      <h1>{title}</h1>
    </header>
  )
}
```

# PropTypes
Kind of like types for your props, makes your code more robust.

As an example, we can add the following import statement to the top of Header.js
```javascript
import PropTypes from 'prop-types'
```

Next we can add the following to indicate that `title` is a string. This goes **above** the export statement as usual.
```jsx

header.defaultProps = {
  title: 'Test defaults',

}
header.propTypes = {
  title: PropTypes.string
}
```

# Styling
You can use stylesheets, use Style Components (external package).
Can use direct CSS in Javascript.

Example:
```jsx
<h1 style={{ color: 'red'}}>{title}</h1>
```
We change the `h1` in Header.js to the above, colors the element to red

Alternatively you can do something like this
```jsx 
<h1 style={headingStyle}>{title}</h1>

const headingStyle = {
  color: 'red',
  backgroundColor: 'black'
}
```


We can use props we pass in to change CSS, refer to [Button.js](./src/components/Button.js)



State gets passed down, actions get passed up