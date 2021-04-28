FROM puckel/docker-airflow:1.10.8

LABEL AWTY "Brian Le, Chad Schadewald, Gary Marmon, Jairun DIemert"

USER root

COPY entrypoint.sh /entrypoint.sh
RUN rm $AIRFLOW_HOME/airflow.cfg

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev libcurl4-openssl-dev libssl-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

USER airflow