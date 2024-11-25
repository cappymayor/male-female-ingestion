import logging

import awswrangler as wr

from .aws import aws_session
from .fetch_data import fetch_users

all_profiles = fetch_users(3000)
male_all_profiles = all_profiles[all_profiles["gender"] == "male"]
female_all_profiles = all_profiles[all_profiles["gender"] == "female"]
bucket = 'dev-male-female-ingestion'
col = {"location.postcode": "string"}    # explicit dtype casting to string


def extract_to_s3():
    logging.info(f"Total number of all_profiles fetched: {len(all_profiles)}")
    wr.s3.to_parquet(
        df=all_profiles,
        path=f"s3://{bucket}/male_female_ingestion/all_profiles",
        boto3_session=aws_session(),
        mode='overwrite',
        dataset=True,
        database='random-profile',
        table='random_profile',
        dtype=col
    )
    return ("Data successfully written to the all all_profiles S3 bucket")


def extract_male_to_s3():
    logging.info(f"Number of male all_profiles: {len(male_all_profiles)}")
    wr.s3.to_parquet(
        df=male_all_profiles,
        path=f"s3://{bucket}/male_female_ingestion/male_all_profiles",
        boto3_session=aws_session(),
        mode='overwrite',
        dataset=True,
        database='random-profile',
        table='male_profile',
        dtype=col
    )
    return ("Data successfully written to the male profile S3 bucket")


def extract_female_to_s3():
    logging.info(f"Number of female all_profiles: {len(female_all_profiles)}")
    wr.s3.to_parquet(
        df=female_all_profiles,
        path=f"s3://{bucket}/male_female_ingestion/female_all_profiles",
        boto3_session=aws_session(),
        mode='overwrite',
        dataset=True,
        database='random-profile',
        table='female_profile',
        dtype=col
    )
    return ("Data successfully written to the female profile S3 bucket")
