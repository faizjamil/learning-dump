// call this file from the commandline
// node s3_delete_object.js <key of file you want to delete>
// for the sake of flexibility and privacy, the code checks for the s3 bucket url to be specified in an environment variable:
// S3_BUCKET: <bucket url> DO NOT INCLUDE HTTP/HTTPS:// at the beginning

import { DeleteObjectCommand} from "@aws-sdk/client-s3";
import { s3Client } from "./s3_client.js";
const S3_BUCKET = process.env.S3_BUCKET
export const objectParams = { 
    Bucket: S3_BUCKET, 
    Key: process.argv[2]

};


export const deleteObject = async () => {
    try {
        const deleteCommand = new DeleteObjectCommand(objectParams);
        const deleteResponse = await s3Client.send(deleteCommand)
        console.log(deleteResponse)

    } catch (error) {
        console.log(error)        
    }

}
deleteObject();