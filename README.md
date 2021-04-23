# AWTY-Limitless

# Executive Summary

With the sports analytics and sports betting industry booming in recent years, there has become a bigger need for
consumers to be able to have access to statistical tools to better inform decision making. Many sources of raw data have
popped up, but not many tools to leverage this data for those who lack the mathematical or programming background. In
response to this need we plan to create an automated pipeline to ingest data from stats sources, combine, clean, and
transform the data. Finally, perform statistical analysis to project NBA seasonal outcomes and persist data in a
database. The data and results will be accessible through a dashboard web app that provides accessibility to those who
would otherwise need extensive knowledge of data gathering and statistical techniques to run such analysis.

<b>To run our project:</b>

1. Install Docker: https://docs.docker.com/engine/install/
2. cd into the project root directory.
3. sudo docker-compose up -d --build
    1. Dash Board
        1. WebApp http://localhost:8050
    2. Airflow Access
        1. Admin http://localhost:8080
        2. Flower http://localhost:5555
    3. NBA database MongoDB
        1. Server Test http://localhost:4321
    4. API Gateway
        1. Server Test http://localhost:9999
    5. Auth Gaurd 
        1. Server Test http://localhost:3000
4. Turn off services.
    2. sudo docker-compose down
