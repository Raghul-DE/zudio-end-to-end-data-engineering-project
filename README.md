# Zudio End-To-End Data Engineering Project
## Introduction:
This project develops an ETL pipeline using the Zudio sales dataset on AWS. It extracts raw sales data from S3, transforms it into structured datasets (Sales Data, Store Info, Inventory Data), and loads the transformed files back into S3. Processed files are archived to prevent reprocessing.

## Use case:
**AI-Driven Inventory Optimization for Fast Fashion Reatilers**

"Retailers struggle with inventory mismanagement, leading to stockouts and excess inventory. My ETL pipeline processes historical Zudio sales data(2024) to forecast demand and optimize inventory levels for 2025."

## About Dataset:
you can download the dataset from this link(for testing purpose),available in the - [zudio_sales_data.csv file](https://www.kaggle.com/datasets/saketkshirsagar1/zudio-sales-test-dataset)

## Architecture:
![Architecture diagram of AWS ETL Pipeline.](https://github.com/Raghul-DE/zudio-end-to-end-data-engineering-project/blob/main/zudio-etl-pipeline-architecture.jpg)

## Services used:
1. **S3 (Simple Storage Service):** Amazon S3 (Simple Storage Service) is a scalable, secure, and durable cloud storage service used to store, manage, and retrieve data like files, images, logs, and datasets.
   - Stores raw Zudio sales data CSV files before processing.
   - Holds transformed and structured data after the ETL process.
   - Acts as a data lake, allowing Athena to query stored data directly.
    
2. **AWS Lambda:** AWS Lambda is a serverless compute service that lets you run code without managing servers. It automatically triggers when a file is uploaded to S3 and scales as needed.
    - Triggered automatically when a new sales data file is uploaded to S3.
    - Runs Python ETL scripts to extract, transform, and structure the data.
    - Saves the cleaned and processed data back into S3 (processed folder).
      
3. **Glue Crawler:** AWS Glue Crawler is a schema discovery tool that automatically scans your data in Amazon S3 and infers its structure (schema).It automates schema management, so you don’t have to define tables manually.
    - Scans structured data in S3 and infers its schema.
    - Creates metadata tables in AWS Glue Data Catalog, making data queryable.
    - Automatically updates when new structured data is added.
      
4. **Data Catlog:** AWS Glue Data Catalog is a fully managed metadata repository that makes easy to discover and manage data in AWS, you can use the Glue Data catlog with other serive's such as Athena.
    - Acts as a centralized metadata repository for structured Zudio sales data.
    - Stores table definitions (e.g., sales_data, store_info, inventory_data).
    - Enables Amazon Athena to query the dataset efficiently.
      
5. **Amazon Athena:** Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. You can use Athena to analyze data stored in your AWS Glue Data Catalog or directly from other S3 buckets.
    - Allows serverless SQL queries on S3-stored data without a traditional database.
    - Helps analyze sales trends, store performance, and inventory insights.
    - Uses the schema defined in AWS Glue Data Catalog for optimized querying.

##Data Flow in the ETL Pipeline:

### Data Ingestion (Raw Data Storage in S3)
The Zudio sales dataset (CSV file) is manually uploaded to an S3 bucket inside the /to_processed/ folder.This serves as the staging area for new data before transformation.

### AWS Lambda - Extract, Transform & Move Processed Data
Lambda Function Trigger:
When a new file is uploaded to /to_processed/, an AWS Lambda function is triggered.

Data Extraction:
The Lambda function reads the CSV file using Pandas and extracts key attributes into structured DataFrames:

 - sales_data_df: Order & transaction details
 - store_info_df: Store metadata
 - store_inventory_df: Inventory & stock details
   
Data Transformation Steps:

Convert Date Format:

 - sales_data_df["Order Date"] = pd.to_datetime(sales_data_df["Order Date"]).Ensures that Order Date is properly formatted as a datetime object for better querying.

Remove Duplicate Records:

 - Duplicates are removed from all three DataFrames (sales_data_df, store_info_df, store_inventory_df).Ensures data consistency and prevents duplicate entries in the processed dataset.

Transformed Data Storage:

 - The cleaned and structured data is stored in S3 under /processed-data/ as partitioned Parquet files, which improve query efficiency.

Cleanup Step (Deleting Processed Files from /to_processed/):

 - Once the transformation is complete and the processed data is successfully stored, Lambda automatically deletes the original file from /to_processed/.This prevents duplicate processing and keeps the pipeline clean.

### AWS Glue Crawler - Schema Inference
The Glue Crawler scans /processed-data/, infers the schema, and creates tables in the Glue Data Catalog.The following structured tables are registered in AWS Glue:

 - sales_data_table → Transformed sales transactions
 - store_info_table → Cleaned store details
 - store_inventory_table → Processed inventory data

### Amazon Athena - Query & Analytics
Athena queries the transformed data stored in S3 using the Glue Data Catalog schema.
Example Use Cases:

 - Track daily, weekly, and monthly sales trends.
 - Identify high-demand products and optimize inventory.
 - Compare store performance across different locations.
 - Generate insights for replenishment and restocking decisions.

## Final Workflow Summary
1️. Raw sales data (CSV) is uploaded to S3 → /to_processed/

2️. AWS Lambda extracts, cleans, and transforms the data.

3️. Transformed data is saved in S3 → /processed-data/ (Parquet format).

4️. AWS Lambda deletes the original file from /to_processed/ to avoid reprocessing.

5️. AWS Glue Crawler updates the Glue Data Catalog with structured tables.

6️. Amazon Athena allows SQL-based analytics on the transformed dataset.


## Install Packages:
```
pip install pandas as pd
```
