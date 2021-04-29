# AWTY-Limitless

Folder Structure
<pre><font color="#3465A4"><b>AWTY-Limitless</b></font>
   ├── <font color="#3465A4"><b>APIGatewayServerContainer</b></font>
   │   ├── <font color="#eb7100"><i>"Code/Scripts to build the Gateway"</i></font>
   ├── <font color="#3465A4"><b>AuthGaurdServerContainer</b></font>
   │   ├── <font color="#eb7100"><i>"Code/Scripts to build the Gaurd"</i></font>
   ├── <font color="#3465A4"><b>ClientServerContainer</b></font>
   │   ├── <font color="#eb7100"><i>"Code/Scripts to build the Dashboard"</i></font>
   ├── <font color="#3465A4"><b>DatabaseServerContainer</b></font>
   │   ├── <font color="#eb7100"><i>"Code/Scripts to build the Database"</i></font>
   ├── <font color="#3465A4"><b>DataServerContainer</b></font>
   │   ├── <font color="#eb7100"><i>"Code/Scripts to build the Scheduler"</i></font>
   ├── docker-compose.yml <font color="#00ebe7"><i>"I build and run it all."</i></font>
   ├── <font color="#b50909"><b>Final_Submission_Artifacts</b></font><font color="#09b531"><b> "GRADE ME"</b></font>
   │   ├── Code_Scripts_DB.txt
   │   ├── <font color="#b50909"><b>Manuals</b></font>
   │   │   ├── <a href="https://docs.google.com/document/d/1AwEcy0xrCWPhNiTXNR9uQQUUTEDDDazsUbc3S3skhzg/edit?usp=sharing" target="_top">Deployment_Installation.txt</a>
   │   │   └── <a href="https://docs.google.com/document/d/1du1nYOVQMsAhM0N5b1_5PZ0YJF5IKCIBt4whIkw76C0/edit?usp=sharing" target="_top">User_Administrator.txt</a>
   │   └── <a href="https://docs.google.com/document/d/1ISOMe2S8vfHr1nAAS4RSGYrfR1yiwgH8JFHY8mfFoHQ/edit?usp=sharing" target="_top">Project_Report.txt</a>
   └── README.md
</pre>
    

# Executive Summary

With the sports analytics and sports betting industry booming in recent years, there has become a bigger need for
consumers to be able to have access to statistical tools to better inform decision making. Many sources of raw data have
popped up, but not many tools to leverage this data for those who lack the mathematical or programming background. In
response to this need we plan to create an automated pipeline to ingest data from stats sources, combine, clean, and
transform the data. Finally, perform statistical analysis to project NBA seasonal outcomes and persist data in a
database. The data and results will be accessible through a dashboard web app that provides accessibility to those who
would otherwise need extensive knowledge of data gathering and statistical techniques to run such analysis.




# Instructions

<b><i>Our project is built using docker containers. Each container can be built and run locally utilizing docker-compose. Once the project is running the different services can be viewed through your web browser.</i></b>

<b>To run our project:</b>

1. Instructions to install docker-compose : 
    * [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/) 

2. Using your Command Line Interface: 
    * cd into the project root directory <i>AWTY-Limitless</i>

3. Run the command: 
    * <i>sudo docker-compose up -d --build</i>

<b>To view our project:</b>

1. Dashboard:
    * WebApp [http://localhost:8050](http://localhost:8050) 

2. Scheduler Airflow Access
    * Admin [http://localhost:8080](http://localhost:8080)
    * Flower [http://localhost:5555](http://localhost:5555) 

3. NBA database MongoDB
    * Server Test [http://localhost:4321](http://localhost:4321)

4. API Gateway
    * Server Test [http://localhost:9999](http://localhost:9999) 

5. Auth Guard
    * Server Test [http://localhost:3000](http://localhost:3000)

<b>To turn off our project:</b>

1. Using your Command Line Interface:
    * <i>sudo docker-compose down</i>
