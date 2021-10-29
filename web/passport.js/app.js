const dotenv = require('dotenv').config()
const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const app = express();
const PORT = process.env.PORT || 3000;
const mongoose = require('mongoose');
const flash = require('connect-flash');
const session = require('express-session');

// passport config
const passport = require('passport')
require('./config/passport')(passport)
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

// bodyparser
app.use(express.urlencoded({ extended: false}))

// Express session middleware
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true,
}));
// passport middleware
app.use(passport.initialize());
app.use(passport.session());
// Connect flash middleware
app.use(flash());

// Global vars
app.use((req, res, next)=> {
    res.locals.success_msg = req.flash('success_msg');
    res.locals.error_msg = req.flash('error_msg');
    res.locals.error = req.flash('error');
    next();
});

// routes

app.use('/', require('./routes/index'));
app.use('/users', require('./routes/users'));
app.listen(PORT, console.log(`server started on http://localhost:${PORT}`))