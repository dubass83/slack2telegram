FROM alpine:3.7
LABEL maintainer="Maks Sych<makssych@gmail.com>"

WORKDIR /usr/src/app
RUN apk add --no-cache \
        python3 python3-dev \
        gcc musl-dev \
        linux-headers libffi-dev libressl-dev
COPY . /usr/src/app
RUN rm -rf public/*
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "bot.py" ]