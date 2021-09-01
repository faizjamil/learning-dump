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

Prior to Reacth 16.8, had to use class based components to use state. 
Now we can use funcitonal components with **hooks**


# React Hooks
Functions that allow us to let us hook into the React state and lifecycle features from function components.

Examples:
* useState - Returns a stateful value and a function to update it
* useEffect - Perform side effects in function components
* useContent, useReducer, useRef, etc.

