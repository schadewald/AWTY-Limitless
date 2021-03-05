# AWTY-Limitless

# Executive Summary

With the sports analytics and sports betting industry booming in recent years, there has become a bigger need for consumers to be able to have access to statistical tools to better inform decision making. Many sources of raw data have popped up, but not many tools to leverage this data for those who lack the mathematical or programming background. In response to this need we plan to create an automated pipeline to ingest data from stats sources, combine, clean, and transform the data. Finally, perform statistical analysis to project NBA seasonal outcomes and persist data in a database. The data and results will be accessible through a dashboard web app that provides accessibility to those who would otherwise need extensive knowledge of data gathering and statistical techniques to run such analysis.

<b>To run our project:</b>

1. Database service
   1. cd into Database Server Container
   2. Build to Docker image.
      1. <i>sudo docker build -t database:latest .</i>
      2. <i>sudo docker run -p 4321:4321 database</i>
   3. Open a browser and visit http://localhost:4321/ to check if service is running.
      1. Load DB with dummy dataset.
         1. http://localhost:4321/db/update
      2. View dataset.
         1. http://localhost:4321/db/retrieve
      3. Clear all data.
         1. http://localhost:4321/db/clear
   4. Turn off database service.
      1. CTRL c
