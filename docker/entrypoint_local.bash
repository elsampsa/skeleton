#!/bin/bash
# you can run this file directly on your local system
# it is also used by docker-compose-local.yml
# with docker-compose-local.yml the local dir is: /usr/src/app/

if [ -f /.dockerenv ]; then
    echo "entrypoint: docker run"
    # -e = development mode install: the current dir is "linked" to your python dependencies directory
    pip3 install --install-option="--separate-cpp-module" --no-dependencies -e /usr/src/app/
    # separate-cpp-module: has been installed separately in the Dockerfile
    # ..that parameter is passed as-is to setup.py
else
    echo "entrypoint: localhost run"
    # we suppose that you have run manually:
    # pip3 install --user -e .
fi

# pip3 install has created this cli command into your system: see
# setup.py: entry_points
skeleton-command run
