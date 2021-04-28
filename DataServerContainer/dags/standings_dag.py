from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from nba_api.stats.endpoints import leaguestandings
import json

default_args = {
    'owner': 'AWTY',
    'start_date': datetime(2021, 1, 1),
    'retries': 2
}

standings_dag = DAG('extract_standings', default_args=default_args, schedule_interval='0 0 * * *')


def get_standings():
    standings = leaguestandings.LeagueStandings(season='2020-21')
    standings = standings.get_normalized_json()
    json_object = json.loads(standings)
    json_formatted_str = json.dumps(json_object, indent=2)
    print("Extracted standings from NBA-API")
    with open('standings_dump.json', 'w') as outfile:
        outfile.write(json_formatted_str)
    return "Populated json_file..."


get_standings_task = PythonOperator(
    task_id='get_standings',
    python_callable=get_standings,
    dag=standings_dag
)

load_standings_task = BashOperator(
    task_id='load_standings',
    bash_command='curl --header "Content-Type: application/json" --request POST --data @/usr/local/airflow/standings_dump.json http://nbadb:4321/db/update',
    dag=standings_dag
)

run_montecarlo_task = BashOperator(
    task_id='run_montecarlo',
    bash_command='python /usr/local/airflow/dags/montecarlo.py',
    dag=standings_dag
)

# cleanup = BashOperator(
#     task_id='cleanup_files',
#     bash_command="rm DataServerContainer/*.json",
#     dag=standings_dag
# )


get_standings_task >> load_standings_task >> run_montecarlo_task
