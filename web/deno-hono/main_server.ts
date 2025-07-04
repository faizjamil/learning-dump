import { Hono } from 'npm:hono';
import api_headers from './lib/api_headers.ts';
const app = new Hono();

app.use('/', api_headers);
app.get('/', (c) => {
  return c.text('Hello Deno!');
});

Deno.serve(app.fetch);