FROM node:26-trixie-slim

RUN npm config set update-notifier false

# install global packages in non-root user directory per: https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#global-npm-dependencies
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

# optionally if you want to run npm global bin without specifying path
ENV PATH=$PATH:/home/node/.npm-global/bin 

# install pnpm
# THIS COMMAND WORKS
RUN npm i -g pnpm@11.28.0
# Using this commands results in an error ERR_PNPM_UNKNOWN_SHELL
# RUN npx --yes get-pnpm
# Using the commands below results in a "pnpm: not found" error when executing pnpm fetch below
# RUN apt-get update && apt-get install -y curl
# RUN curl -fsSL https://get.pnpm.io/install.sh | ENV="$HOME/.bashrc" SHELL="$(which bash)" bash -

# Set up directories in advance so we can control the permissions
RUN mkdir -p /usr/app/node_modules && chown -R node:node /usr/app

# Set the work directory
WORKDIR /usr/app

# Set the user
USER node

## Dependencies are handled in their own layer so that we can leverage layer cache and save time on rebuild

# Copy over the dependencies
COPY --chown=node:node package.json .
COPY --chown=node:node pnpm-lock.yaml .
COPY --chown=node:node pnpm-workspace.yaml .
# silence npm update notifs when using npx
RUN npm config set update-notifier false

# fetch dependencies to content addressable store
RUN pnpm fetch

# Install the dependencies
RUN pnpm install --offline --frozen-lockfile

# Copy over application files
COPY --chown=node:node . .

# Set ARGs and ENV vars
ARG BUILD_VERSION
ARG ENV

ENV ENV=${ENV}
ENV BUILD_VERSION=${BUILD_VERSION}
ENV NODE_ENV=${ENV}

# If this is a prod environment, package the code
RUN if [ "$ENV" != "local" ]; then node --run lint; fi

# Start the service
CMD ["bash", "./start-service"]
