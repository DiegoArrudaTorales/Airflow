from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("my_dag",start_date=datetime(2021, 1, 1),
         schedule_interval="@daily", catchup=False) as dag:

training_model_A = PythonOperator(
    task_id="training_model_A"
    python_callable=print_hi("Diego")

)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
