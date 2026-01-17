import cookieParser from 'cookie-parser';
import express from 'express';
import logger from 'morgan';

import indexRouter from './routes/index.js';
import usersRouter from './routes/users.js';

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static('./public'));

app.use('/', indexRouter);
app.use('/users', usersRouter);

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
export default app;
