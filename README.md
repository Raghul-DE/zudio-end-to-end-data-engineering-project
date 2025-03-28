# Zudio End-To-End Data Engineering Project
## Introduction:
This project develops an ETL pipeline for retail sales analytics using AWS. It processes Zudio’s 2024 sales dataset, which is manually uploaded to S3. AWS Lambda extracts and transforms the data into structured datasets (Sales Data, Store Info, Inventory Data) before loading the processed files into an S3 processed/ folder. AWS Glue catalogs the data, enabling querying and analysis using Athena.

## Use case:
**AWS-Based Sales Data Processing Pipeline for Retail Analytics**

"Retailers need structured sales and inventory data to track performance and identify trends. My ETL pipeline processes historical Zudio sales data (2024) and organizes it into a structured format for easier querying and analytics using AWS services. This helps retailers gain insights into sales trends, store performance, and inventory distribution."

## About Dataset:
you can download the dataset from this link(for testing purpose),available in the - [zudio_sales_data.csv file](https://www.kaggle.com/datasets/saketkshirsagar1/zudio-sales-test-dataset)

## Architecture:
![Architecture diagram of AWS ETL Pipeline.](https://github.com/Raghul-DE/zudio-end-to-end-data-engineering-project/blob/main/zudio-etl-pipeline-architecture.jpg)

## Services used:
1. **S3 (Simple Storage Service):** Amazon S3 (Simple Storage Service) s a scalable, secure, and durable cloud storage service for storing, managing, and retrieving data such as files, images, logs, and datasets.
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

## Data Flow in the ETL Pipeline

### - Data Ingestion (Raw Data Storage in S3):
The Zudio sales dataset (CSV file) is manually uploaded to an S3 bucket inside the /to_processed/ folder.This serves as the staging area for new data before transformation.

### - AWS Lambda - Extract, Transform & Move Processed Data:
Lambda Function Trigger:
When a new file is uploaded to /to_processed/, an AWS Lambda function is triggered.

**Data Extraction:**
The Lambda function reads the CSV file using Pandas and extracts key attributes into structured DataFrames:

 - sales_data_df: Order & transaction details
 - store_info_df: Store metadata
 - store_inventory_df: Inventory & stock details
   
**Data Transformation Steps:**

 - Convert Date Format: sales_data_df["Order Date"] = pd.to_datetime(sales_data_df["Order Date"]).Ensures that Order Date is properly formatted as a datetime object for better querying.

 - Remove Duplicate Records: Duplicates are removed from all three DataFrames (sales_data_df, store_info_df, store_inventory_df).Ensures data consistency and prevents duplicate entries in the processed dataset.

**Transformed Data Storage:**

 - The cleaned and structured data is stored in S3 under /processed-data/ as partitioned Parquet files, which improve query efficiency.

**Cleanup Step (Deleting Processed Files from /to_processed/):**

 - Once the transformation is complete and the processed data is successfully stored, Lambda automatically deletes the original file from /to_processed/.This prevents duplicate processing and keeps the pipeline clean.

### - AWS Glue Crawler - Schema Inference:
The Glue Crawler scans /processed-data/, infers the schema, and creates tables in the Glue Data Catalog.The following structured tables are registered in AWS Glue:

 - sales_data_table → Transformed sales transactions
 - store_info_table → Cleaned store details
 - store_inventory_table → Processed inventory data

### - Amazon Athena - Query & Analytics:
Athena queries the transformed data stored in S3 using the Glue Data Catalog schema.
Example Use Cases:

 - Track daily, weekly, and monthly sales trends.
 - Identify high-demand products and optimize inventory.
 - Compare store performance across different locations.
 - Generate insights for replenishment and restocking decisions.

## Final Workflow Summary:
1️. Raw sales data (CSV) is uploaded to S3 → /to_processed/

2️. AWS Lambda extracts, cleans, and transforms the data.

3️. Transformed data is saved in S3 → /processed-data/ (Parquet format).

4️. AWS Lambda deletes the original file from /to_processed/ to avoid reprocessing.

5️. AWS Glue Crawler updates the Glue Data Catalog with structured tables.

6️. Amazon Athena allows SQL-based analytics on the transformed dataset. 

### Conclusion:

This project successfully builds an AWS-based ETL pipeline to process and analyze Zudio’s 2024 sales data for better inventory and sales insights. By leveraging S3, Lambda, Glue, and Athena, we have automated data ingestion, transformation, and querying, enabling structured data-driven decision-making.

- Automated & Scalable Data Processing – AWS Lambda AWS Lambda automates data transformation and loading (ETL) after manual file upload.
- Centralized Data Storage – Processed sales data is stored in Amazon S3 and cataloged in AWS Glue, ensuring structured data management.
- Retail Analytics with Athena – Businesses can use SQL queries in Athena to analyze sales trends, store performance, and product demand.

This pipeline helps fast fashion retailers by providing structured sales and inventory data to improve decision-making.

### Important Note:
**Manual File Upload:** While the ETL pipeline is fully automated after the file is uploaded to S3, the file upload process itself is manual. Currently, the sales dataset (CSV) needs to be manually placed in the /to_processed/ folder in S3 for the pipeline to trigger.




## Install Packages:
```
pip install pandas as pd
```
