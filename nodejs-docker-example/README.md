# Minimal Docker Node.js example

This is an example of trying to install pnpm using the official node.js Docker image

This is based off of [the instructions on Docker's official node.js tutorial](https://docs.docker.com/guides/nodejs/#create-the-docker-assets) with some modifications based on the container workflow my employer uses.

As is when building this service you will not get any errors since we are installing pnpm **v11**.

Comments are included in the `Dockerfile` accordingly describing the two official ways to install pnpm without using the suggested pnpm docker image (mainly cause I don't know how to run the code without root using that image).