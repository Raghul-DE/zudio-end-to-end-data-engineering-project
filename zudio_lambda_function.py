import json
import os
import boto3
import pandas as pd
from io import StringIO


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    BUCKET_NAME = os.environ['BUCKET_NAME']
    RAW_DATA_PREFIX = "raw_data/to_processed/"
    PROCESSED_PATH = "raw_data/processed/"
    TRANSFORMED_PATH = "transformed_data/"

    response = s3.list_objects(Bucket=BUCKET_NAME, Prefix=RAW_DATA_PREFIX)
    if "Contents" not in response:
        print("No new files found.")
        return
    
    files = [obj["Key"] for obj in response["Contents"]]
    print("Files found:", files)
    
    for file_key in files:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)  # Read the CSV file
        csv_content = response["Body"].read().decode("utf-8")  # Decode to string
        #print(f"CSV Content of {file_key}:\n", csv_content)
        
        if not csv_content.strip():
            print(f"Skipping empty file: {file_key}")
            continue

        # Read CSV into DataFrame
        df = pd.read_csv(StringIO(csv_content))
        
        print(f"CSV Loaded Successfully: {file_key}")
        print(df.head())  # Print first few rows

        # Apply transformations
        sales_data_df= df[["Store", "Order ID", "Order Date", "Product ID", "Price", "Quantity", "Sales Profit"]]
        sales_data_df["Order Date"] = pd.to_datetime(sales_data["Order Date"])
        sales_data_df = sales_data_df.drop_duplicates()
        if store_info_df.isna().any().any():
            print("missing value dedected")
        else:
            print ("no missing value")

        


        store_info_df= df[["Store", "Country", "State", "City", "Store Number", "Store Type", "Store Open Date"]]
        store_info_df = store_info_df.drop_duplicates()
        if store_info_df.isna().any().any():
            print("missing value dedected")
        else:
            print ("no missing value")

        store_inventory_df = df[["Store", "Category", "Clothing Type", "Product ID", "Price", "Quantity"]]
        store_inventory_df = inventory_df.drop_duplicates()
        if store_inventory_df.isna().any().any():
            print("missing value dedected")
        else:
            print ("no missing value")

        # Save transformed data back to S3
        save_to_s3(s3, sales_data_df, BUCKET_NAME, TRANSFORMED_PATH + "sales_data/" + file_key.split("/")[-1])
        save_to_s3(s3, store_info_data_df, BUCKET_NAME, TRANSFORMED_PATH + "store_info_data/" + file_key.split("/")[-1])
        save_to_s3(s3, store_inventory_df, BUCKET_NAME, TRANSFORMED_PATH + "inventory_data/" + file_key.split("/")[-1])

        # Move processed file to processed folder
        processed_file_key = PROCESSED_PATH + file_key.split("/")[-1]
        s3.copy_object(Bucket=BUCKET_NAME, CopySource={'Bucket': BUCKET_NAME, 'Key': file_key}, Key=processed_file_key)
        s3.delete_object(Bucket=BUCKET_NAME, Key=file_key)
        print(f"Moved {file_key} to {processed_file_key}")

def save_to_s3(s3_client, dataframe, bucket_name, key):
    """Helper function to save DataFrame to S3 as CSV."""
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())
