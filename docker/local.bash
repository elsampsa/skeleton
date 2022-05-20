#!/bin/bash
## if you'd like to include an env file, could do this:
# docker-compose -f docker-compose-local.yml -p local --env-file /path/to/local.env $@
## that "local" is added to the name of the containers
set -a
docker-compose -f docker-compose-local.yml -p local $@
set +a
