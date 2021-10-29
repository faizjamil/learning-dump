import * as fs from "node:fs/promises";

async function openFile() {
    try {
        const csvHeaders = 'name,quantity,price';
        await fs.writeFile('groceries.csv', csvHeaders);
    } catch (error) {
        console.error(`Got an error trying to write to a file: ${error.message}`);
    }
}
async function addGroceryItem(name,quantity,price) {
    try {
        const csvLine = `\n${name},${quantity},${price}`;
        // flags: a = append to file, if no flag specified, defaults to w (write) flag which overwrites a file
        await fs.writeFile('groceries.csv', csvLine, { flag: 'a'});
    } catch (error) {
        console.error(`Got an error trying to write to a file: ${error.message}`);
    }
}

(async function () {
    await openFile();
    await addGroceryItem('eggs', 12, 1.50);
    await addGroceryItem('nutella', 1, 4);
})();