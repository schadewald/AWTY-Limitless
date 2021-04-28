FROM python:3

LABEL AWTY "Brian Le, Chad Schadewald, Gary Marmon, Jairun DIemert"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY requirements.txt /APIGatewayServerContainer/requirements.txt

WORKDIR /APIGatewayServerContainer

RUN pip3 install -r requirements.txt

COPY . /APIGatewayServerContainer

ENTRYPOINT [ "python3" ]

CMD [ "gateway.py" ]
