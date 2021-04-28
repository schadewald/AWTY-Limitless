FROM python:3

LABEL AWTY "Brian Le, Chad Schadewald, Gary Marmon, Jairun DIemert"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev curl

COPY requirements.txt /ClientServerContainer/requirements.txt

WORKDIR /ClientServerContainer

RUN pip3 install -r requirements.txt

COPY . /ClientServerContainer

ENTRYPOINT [ "python3" ]

CMD [ "dashboard.py" ]
