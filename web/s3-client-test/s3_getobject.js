import { GetObjectCommand } from "@aws-sdk/client-s3";
import { s3Client } from "./s3_client.js";

const S3_BUCKET = process.env.S3_BUCKET
export const objectParams = { 
    Bucket: S3_BUCKET, 
    Key: "/image-service//webp/cdn.newsday.com/polopoly_fs/1.21795386.1539257367!/httpImage/image.jpg_gen/derivatives/display_1004/image.jpg"

};

export const run = async () => {
    try {
        // Create a helper function to convert a ReadableStream to a string.
        const streamToString = (stream) =>
          new Promise((resolve, reject) => {
            const chunks = [];
            stream.on("data", (chunk) => chunks.push(chunk));
            stream.on("error", reject);
            stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
          });
    
        // Get the object} from the Amazon S3 bucket. It is returned as a ReadableStream.
        const data = await s3Client.send(new GetObjectCommand(objectParams));
          // return data; // For unit tests.
        // Convert the ReadableStream to a string.
        const bodyContents = await streamToString(data.Body);
        console.log(bodyContents);
          // return bodyContents;
      } catch (err) {
        console.log("Error", err);
      }

};
run();