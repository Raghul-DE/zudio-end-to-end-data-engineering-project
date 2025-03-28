# Zudio End-To-End Data Engineering Project
### Introduction:
This project builds an ETL pipeline using the Zudio sales dataset on AWS. It extracts raw sales data from S3, transforms it into structured datasets (Sales Data, Store Info, Inventory Data), and loads the transformed files back into S3. Processed files are archived to prevent reprocessing.

### Use case:
**AI-Driven Inventory Optimization for Fast Fashion Stores**

"Retailers struggle with inventory mismanagement, leading to stockouts and excess inventory. My ETL pipeline processes historical Zudio sales data(2024) to forecast demand and optimize inventory levels for 2025."

### About Dataset:
This dataset contains Zudio sales information - [zudio_sales_data.csv file](https://github.com/Raghul-DE/zudio-end-to-end-data-engineering-project/blob/main/Zudio_sales_data.csv).

### Architecture:
![Architecture diagram of AWS ETL Pipeline.](https://github.com/Raghul-DE/zudio-end-to-end-data-engineering-project/blob/main/zudio-etl-pipeline-architecture.jpg)

### Services used:
1. **S3 (Simple Storage Service):** Amazon S3 (Simple Storage Service) is a scalable, secure, and durable cloud storage service used to store, manage, and retrieve data like files, images, logs, and datasets.
  
2. **AWS Lambda:** AWS Lambda is a serverless compute service that lets you run code without managing servers. It automatically triggers when a file is uploaded to S3 and scales as needed.

3. **Glue Crawler:** AWS Glue Crawler is a schema discovery tool that automatically scans your data in Amazon S3 and infers its structure (schema).It automates schema management, so you don’t have to define tables manually.

4. **Data Catlog:** AWS Glue Data Catalog is a fully managed metadata repository that makes easy to discover and manage data in AWS, you can use the Glue Data catlog with other serive's such as Athena.

5. **Amazon Athena:** Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. You can use Athena to analyze data stored in your AWS Glue Data Catalog or directly from other S3 buckets.

### Install Packages:
```
pip install pandas as pd
```
