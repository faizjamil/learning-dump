import { ListBucketsCommand } from "@aws-sdk/client-s3";
import { s3Client } from "./s3_client.js";
export const run = async () => {
    try {
        const data = await s3Client.send(new ListBucketsCommand({}));
        console.log("Success", data.Buckets);
        return data; // for unit tests
    } catch (error) {
        console.log("Error", error);
    };
    
};
run();
