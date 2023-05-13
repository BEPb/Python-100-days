# Select, From & Where
from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "openaq" dataset
dataset_ref = client.dataset("openaq", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# Construct a reference to the "global_air_quality" table
table_ref = dataset_ref.table("global_air_quality")

# API request - fetch the table
table = client.get_table(table_ref)

# Preview the first five lines of the "global_air_quality" table
client.list_rows(table, max_results=5).to_dataframe()

# Query to select countries with units of "ppm"
first_query = """
              SELECT country
              FROM `bigquery-public-data.openaq.global_air_quality`
              WHERE unit = "ppm"
              """

# Set up the query (cancel the query if it would use too much of
# your quota, with the limit set to 10 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
first_query_job = client.query(first_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
first_results = first_query_job.to_dataframe()

# View top few rows of results
print(first_results.head())

# Query to select all columns where pollution levels are exactly 0
zero_pollution_query = """
                       SELECT *
                       FROM `bigquery-public-data.openaq.global_air_quality`
                       WHERE value = 0
                       """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(zero_pollution_query, job_config=safe_config)

zero_pollution_results = query_job.to_dataframe()

print(zero_pollution_results.head())

