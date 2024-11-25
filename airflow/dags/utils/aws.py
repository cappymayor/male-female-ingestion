import boto3
from airflow.models import Variable


# Establish connection with AWS and Extract files to AWS S3
def aws_session():
    session = boto3.Session(
                aws_access_key_id=Variable.get('aws_access_key'),
                aws_secret_access_key=Variable.get('aws_secret_key'),
                region_name="eu-north-1"
    )
    return session
