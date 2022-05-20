#!/bin/bash
## if you'd like to include an env file, could do this:
# docker-compose -f docker-compose-remote.yml -p remote --env-file /path/to/remote.env $@
## "remote" is added to the name of the containers
set -a
docker-compose -f docker-compose-remote.yml -p remote $@
set +a
