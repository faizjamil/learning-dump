import { s3Client } from "./s3_client.js";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
const S3_BUCKET = process.env.S3_BUCKET
import fetch from "node-fetch";
export const objectParams = { 
    Bucket: S3_BUCKET, 
    Key: process.argv[2]

};

export const run = async () => {
    // Create a PUT presigned URL
    try {
        // create the command
        const putCommand = new PutObjectCommand({
            Bucket: objectParams.Bucket,
            Key: "test.jpg"
        });

        const putUrl = await getSignedUrl(s3Client, putCommand, { expiresIn: 3600 });
        const putResponse = await fetch(putUrl);
        console.log(
           `\n signed URL: ${await putUrl}\n`
        );
        console.log(putResponse)
    } catch (err) {
        console.log("Error creating presigned URL", err);
    }
    
}

run();