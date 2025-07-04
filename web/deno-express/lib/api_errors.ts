// @ts-types="npm:@types/express@4.17.23"

/**
 * Error handling for requests
 *
 * err.status - HTTP status code
 *
 * err.statusCode - alias for status
 *
 * err.name - Error type corresponding to status code
 *
 * err.message - Message included with error (second param of createError function call)
 * types below are ExpressJS-specific types (besides Error)
 *
 * [Express.js docs for more info](https://expressjs.com/en/guide/error-handling.html)
 */
export default function api_errors(err: any, _req: any, res: any) {
  console.log('Routed to error handler', err);
  res.status(err.statusCode || 500).json({ success: false, error: err });
}
