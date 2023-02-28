#!/bin/bash
mkdir dockerized
mv * dockerized/
mv dockerized skeleton
mkdir datashare
mkdir secrets
ln -s $PWD/skeleton/docker/docker-compose-dev.yml .
cp $PWD/skeleton/skeleton/ini/default.ini secrets/dev.ini
ln -s $PWD/skeleton/bash/dev.bash .
#
# now we have:
#
# skeleton/  docker dir
#    docker-compose-dev.yml # --softlinked-to--> (A)
#    dev.bash               # --softlined-to--> (B)
#    secrets/dev.ini        # --softlinked-to--> (C)
#    skeleton/              # python package dir
#        setup.py
#        docker/
#           docker-compose-dev.yml 
#                           # (A)
#        skeleton/          # python code dir
#           ini/default.ini # (B)
#        bash/              # helper script dir
#           dev.bash        # (C)
