export function createHandler(...middleware) {

    return  nextConnect().use(databaseMiddleware, ...middleware);
  
}