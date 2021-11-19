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