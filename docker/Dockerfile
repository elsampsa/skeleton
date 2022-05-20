FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Finland

RUN apt-get update -y && \
    apt-get install -y tzdata && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y ffmpeg libsm6 libxext6 libx264-dev build-essential swig && \
    apt-get install -y dos2unix

RUN pip3 install --upgrade pip
RUN pip3 install numpy 
# ..numpy required before we can compile our custom cpp module for python3

COPY ./requirements.txt /tmp/requirements.txt
# install dependencies
WORKDIR /tmp
RUN pip3 install -r requirements.txt
# the app itself will be installed in development / hot-reload mode

# copy cpp extension in place, compile & install it
ADD skeleton_cpp /tmp/skeleton_cpp
WORKDIR /tmp/skeleton_cpp
RUN pip3 install -vvv .

WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE 1
# here, emphasis on the UN word:
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["bash","/usr/src/app/docker/entrypoint_local.bash"]
# WARNING: docker-compose-local.yml may overwrite the entry point

# interactive session with docker-compose:
# docker-compose run --entrypoint /bin/bash myapp
