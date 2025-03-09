import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from utils.random_profile import (extract_female_to_s3, extract_male_to_s3,
                                  extract_to_s3)

DAG_ID = '_male_female_ingestion'

default_args = {
    'owner': 'dpe-team',
    'start_date': datetime.datetime(2024, 11, 5),
    'retries': 1,
    'retry_delay': datetime.timedelta(seconds=5)
}


dag = DAG(
    DAG_ID,
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False,
    default_view="graph"
)

extract_profile_to_s3 = PythonOperator(
    dag=dag,
    task_id='extract_profile_to_s3',
    python_callable=extract_to_s3
)

extract_male_profile_to_s3 = PythonOperator(
    dag=dag,
    task_id='extract_male_profile_to_s3',
    python_callable=extract_male_to_s3
)

extract_female_profile_to_s3 = PythonOperator(
    dag=dag,
    task_id='extract_female_profile_to_s3',
    python_callable=extract_female_to_s3
)

extract_profile_to_s3 >> \
    [extract_male_profile_to_s3, extract_female_profile_to_s3]
