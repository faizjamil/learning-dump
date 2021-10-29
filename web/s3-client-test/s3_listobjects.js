import { ListObjectsCommand } from "@aws-sdk/client-s3";
import { s3Client } from "./s3_client.js";
const S3_BUCKET = process.env.S3_BUCKET
export const bucketParams = { Bucket: S3_BUCKET}
export const run = async () => {
    try {
        const data = await s3Client.send(new ListObjectsCommand(bucketParams));
        console.log("Success", data);
        return data; // for unit tests
    } catch (error) {
        console.log("Error", error);
    };
    
};
run();