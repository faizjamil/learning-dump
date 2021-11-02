import { DeleteObjectCommand, GetObjectCommand, PutObjectCommand } from "@aws-sdk/client-s3";
import { s3Client } from "./s3_client.js";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
const S3_BUCKET = process.env.S3_BUCKET
import fetch from "node-fetch";
export const objectParams = { 
    Bucket: S3_BUCKET, 
    Key: "test.jpg"

};

export const run = async () => {
    // Create a presigned URL
    try {
        // create the command
        // const command = new GetObjectCommand(objectParams);
        const deleteCommand = new DeleteObjectCommand(objectParams);
        const response = await s3Client.send(deleteCommand)
        console.log(response)
        // Create the presigned URL
        // const signedURL = await getSignedUrl(s3Client, command, {
        //     expiresIn: 3600,
        // });
        // console.log(
        //     `\nGetting "${objectParams.Key}" using signedURL in v3`
        // )
        // console.log(signedURL);
        // const response = await fetch(signedURL);
        // console.log(
        //     `\nResponse returned by signed URL: ${await response}\n`
        // );
        // const putCommand = new PutObjectCommand({
        //     Bucket: objectParams.Bucket,
        //     Key: "test.jpg"
        // });
        // // ContentType: "multipart/form-data"

        // const putUrl = await getSignedUrl(s3Client, putCommand, { expiresIn: 3600 });
        // const putResponse = await fetch(putUrl);
        // console.log(
        //     `\n signed URL: ${await putUrl}\n`
        // );
        // console.log(putResponse)
        //debugger;
    } catch (err) {
        console.log("Error creating presigned URL", err);
    }
    
}
run();