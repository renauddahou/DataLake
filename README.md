# DataLake
Implementation of S3 based Data Lake on AWS Cloud to Aggregate Data from Multiple Sources

A Data Ingestion Framework that automates, the process of pulling semistructured and unstructured data through web scrapping and structured data from RDS, storing it into AWS S3 bucket using PySpark. The Ingestion Framework also incrementally appends the newly generated data into S3 bucket and for Monitoring, Created access Log table in Dynamo DB/GLUE using API Gateway which triggers Lambda service in AWS.

Technologies used:

1.AWS Services(EMR,API Gateway,CFT,IAM,RDS,Lambda,S3), 

2.Python 

3.PySpark

4.Linux
