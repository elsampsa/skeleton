Create a ``main_dir`` & copy the file ``docker-compose-local.yml`` in there.

This would be the main base directory for your fullstack app, while the python package/microservice
resides in ``skeleton``:
```
main_dir/

    docker-compose-local.yml

    secrets/                secrets, configuration files, etc. please do screw environmental variables

    skeleton/               all paths in docker-compose-local.yml relative to this
                            all under this directory copied to docker context
                            mounted to /usr/src/app/

        docker/
                Dockerfile     dockerfile used by docker-compose-local.yml

                entrypoint_local.bash
                            starts the program in the container
                            can also be used for running natively
                                

        requirements.txt       python packages installed into the container

```

- All library dependencies & other "static" stuff (including the cpp extension) is dealt with in ``Dockerfile``
and installed on the image.

- The source code (which you are constantly modifying) is mounted from your local filesystem into the running container.

This way you get best of the both worlds.

With this scheme you can run the fullstack app locally in your pc either natively or using docker-compose.  You can also
run it at the remote site and in cloud.

