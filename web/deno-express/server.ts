// @ts-types="npm:@types/express@4.17.15"
// entry file
import express from 'express';
import cookieParser from 'cookie-parser';
import morgan from 'morgan';
import apiRouter from './routes/api.ts';
import api_headers from './lib/api_headers.ts';
import api_errors from './lib/api_errors.ts';

const app = express();

app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/api', api_headers, apiRouter, api_errors);
app.get('/', (_req: any, res: any) => {
  res.send('<h1>Microservice is running</h1>');
});

app.listen(3000, () => {
  console.log('Service running on port 3000');
});

export default app;
