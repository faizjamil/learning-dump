import * as fs from "node:fs/promises"

async function readFile(filePath) {
    try {
        const data = await fs.readFile(filePath);
        console.log(data.toString())
    } catch (error) {
        console.log("Got an error reading the file: ", error)
    }
};
readFile("greetings.txt")