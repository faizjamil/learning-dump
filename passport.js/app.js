const dotenv = require('dotenv').config()
const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const app = express();
const PORT = process.env.PORT || 3000;
const mongoose = require('mongoose');
// DB config
// DO NOT USE THE COMMENTED OUT LINE, USE ENV VARIABLES
//const db = require('./config/keys').MongoURI()
const db = process.env.MONGODB_URI;

// Connect to Mongo
mongoose.connect(db, { useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => console.log('mongodb connected'))
    .catch(err => console.log(err));

// EJS
app.use(expressLayouts);
app.set('view engine', 'ejs');

// routes

app.use('/', require('./routes/index'));
app.use('/users', require('./routes/users'));
app.listen(PORT, console.log(`server started on port ${PORT}`))