FROM ubuntu:18.04

LABEL maintainer="yannick.feler@gmail.com"


RUN apt-get update -y && apt-get install -y python3 python3-all-dev python3-pip build-essential

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]


CMD [ "madras_app.py" ]