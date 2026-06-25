from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime

# DAG definition to orchestrate the cleaning task
with DAG('clean_data_dag', start_date=datetime(2026, 1, 1), schedule_interval=None, catchup=False) as dag:
    # SSHOperator connects to spark_client to run the cleaning script
    run_cleaning = SSHOperator(
        task_id='run_spark_script',
        ssh_conn_id='spark_client_conn',
        command='python3 /dataops/dags/clean_data.py'
    )