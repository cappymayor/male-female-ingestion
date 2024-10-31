# male-female-ingestion

- This projects aim is to ingest 3000 random profile from this API https://randomuser.me/
  - Extract female and male seprately from the overall 3000.
- Ingest all the profiles into a unified s3 bucket
  - Within the bucket, you can have a folder called `male_profile` and the second one called `female_profile`
  - You should dynamically write to those folders
- Register all objects in the Glue Data Clatalog programatically
- Ensure you are able to query the objects in Athena

## NOTE
- All infrastructure have to be Terraformed
- Airflow to be used for Orchestration
- All Code have to be decently written
- Please apply Linting locally before pushing for better code readability.
