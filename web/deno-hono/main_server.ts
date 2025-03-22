import { Hono } from 'npm:hono'

const app = new Hono()

app.get('/', (c) => {
  return c.text('Hello Deno!')
})

Deno.serve(app.fetch)