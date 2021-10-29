import { S3Client } from "@aws-sdk/client-s3";
// bucket name: https://assets.projects.newsday.com/
// Create an S3 client in the us-east-1 region
// DC_HOST = region such as 'us-west-1'
const DC_HOST = process.env.DC_HOST
const s3Client = new S3Client({
    region: DC_HOST
});
export { s3Client };