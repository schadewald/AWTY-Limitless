FROM python:3

LABEL "value" AWTY "Brian Le, Chad Schadewald, Gary Marmon, Jairun DIemert"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY requirements.txt /DatabaseServerContainer/requirements.txt

WORKDIR /DatabaseServerContainer

RUN pip3 install -r requirements.txt

COPY . /DatabaseServerContainer

ENTRYPOINT [ "python3" ]

CMD [ "database.py" ]