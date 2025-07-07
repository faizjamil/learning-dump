FROM denoland/deno:2.4.0

# ONLY COMMENT OUT ANY COMMANDS BELOW IF THERE IS A PERMS ISSUE
# Set up directories in advance so we can control the permissions
# DON'T RUN UNLESS PERMS ISSUE
# RUN mkdir -p /usr/app/bin && mkdir -p /usr/app/node_modules && chown -R node:node /usr/app

# Set the work directory
WORKDIR /usr/app

# Set the user
USER deno

## Dependencies are handled in their own layer so that we can leverage layer cache and save time on rebuild

# Copy over the dependencies
# COPY --chown=node:node package.json .
# COPY --chown=node:node yarn.lock .
COPY deno.json .
COPY deno.lock .
# Install the dependencies
RUN deno install --frozen
# Copy over application files
# COPY --chown=node:node . .
COPY  . .
# Set ARGs and ENV vars
ARG BUILD_VERSION
ARG ENV

ENV ENV=${ENV}
ENV BUILD_VERSION=${BUILD_VERSION}
ENV NODE_ENV=${ENV}

# Optional environment variables
# Set to disable checking if a newer Deno version is available
ENV DENO_NO_UPDATE_CHECK=1
# Set to disable permission prompts on access
ENV DENO_NO_PROMPT=1

# If this is a prod environment, package the code
# NO BUILD COMMAND FOR DENO RIGHT NOW
# RUN if [ "$ENV" != "local" ]; then deno run build; fi

# Start the service
CMD ["bash", "./start-service"]
