FROM python:3

LABEL AWTY "Brian Le, Chad Schadewald, Gary Marmon, Jairun DIemert"

WORKDIR /AuthGaurdServerContainer

#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
ADD requirements.txt /AuthGaurdServerContainer
RUN pip install --no-cache-dir -r requirements.txt

ADD . /AuthGaurdServerContainer
CMD python gaurd.py

EXPOSE 3000
