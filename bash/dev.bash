#!/bin/bash
cp $PWD/skeleton/skeleton/ini/default.ini secrets/dev.ini
docker-compose -f docker-compose-dev.yml $@
