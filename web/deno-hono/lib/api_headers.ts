import { createMiddleware } from 'hono/factory';
import process from "node:process";

// we want to conditionally add CORS headers


export default createMiddleware(async (c, next) => {
  let origin = c.req.header('origin');
  if (origin && !/newsday/i.test(origin)) {
    origin = undefined;
  }
  if (origin && !/https?:\/\//i.test(origin)) {
    origin = `https://${origin}`;
  }
  // const custom_headers = {
  //   'Cache-Control': ''
  // };

  const custom_headers = {
    'Cache-Control': process.env.ENV === 'local' ? 'no-cache' : 'public, max-age=120, s-maxage=120'
  };
  if (process.env.ENV === 'local') {
    custom_headers['Cache-Control'] = 'no-cache';
  }
  const cors_headers = {};

  if (origin) {
    Object.assign(cors_headers, {
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': origin
    });
  }

  const response_headers: HeadersInit = {
    'Content-Type': 'application/json',
    'x-build-version': process.env.BUILD_VERSION ? process.env.BUILD_VERSION : '',
    ...cors_headers,
    ...custom_headers
  };

  Object.keys(response_headers).filter(key => !!response_headers[key]).forEach(h => {
    c.header(h, response_headers[h]);
  });
  // c.header('Cache-Control', 'no-max');
  await next();
});