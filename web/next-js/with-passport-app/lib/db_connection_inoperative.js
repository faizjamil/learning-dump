/**
 * Generates the appropriate mongo connection string by environment
 *
 * mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
 */

// Modified version of TC's code
import mongoose, {ConnectOptions} from 'mongoose';

async function dbConnect() {
//   const { MONGO_HOST, MONGO_USER, MONGO_PASS, MONGO_PORT }=
//     process.env;
    const MONGO_HOST = "localhost"
    const MONGO_PORT = "27017"
    const MONGO_USER = ""
    const conn_str = ["mongodb://"];
    const conn_query_params = [];
    const RDS_CERT = "";
    if (MONGO_USER) {
      conn_str.push(`${MONGO_USER}:${encodeURIComponent(MONGO_PASS)}@`);
    }
  
    conn_str.push(`${MONGO_HOST}/nd_users`);
  
    if (MONGO_USER) {
      conn_query_params.push(`authSource=${MONGO_USER}`);
    }
  
    if (RDS_CERT) {
      conn_query_params.push("tls=true");
      conn_query_params.push(`tlsCAFile=${RDS_CERT}`);
      conn_query_params.push("retryWrites=false");
    }
  
    if (process.env.ENV === "prod") {
      conn_query_params.push("replicaSet=rs0");
      conn_query_params.push("readPreference=secondaryPreferred");
    }
  
    if (conn_query_params.length > 0) {
      //conn_query_params = conn_query_params.join("&");
      const queryParamsString = conn_query_params.join("&");
      conn_str.push(`?${queryParamsString}`);
    }
  
    //conn_str = conn_str.join("");
    const connectionString = conn_str.join("");
    // TODO: rework these options for latest version of Mongoose and MongoDB
    // Docs on the old options: https://mongoosejs.com/docs/5.x/docs/connections.html
    // Docs on the new options: https://mongoosejs.com/docs/connections.html
    const connectionOptions = {
      maxPoolSize: 10,
      // useNewUrlParser: true,
      // useUnifiedTopology: true, // False by default. Set to true to opt in to using the MongoDB driver's new connection management engine. You should set this option to true, except for the unlikely case that it prevents you from maintaining a stable connection.
      // useFindAndModify: false,
      socketTimeoutMS: 1000 * 60,
    };
    await mongoose.connect(connectionString, connectionOptions);
    console.log('db connected');
 
}
export {
  dbConnect
};
  