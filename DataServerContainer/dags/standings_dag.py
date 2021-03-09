from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
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
    # df_standings = standings.get_data_frames()[0] #standings in table form
    print("Extracted standings from NBA-API")
    with open('DataServerContainer/standings_dump.json', 'w') as outfile:
        json.dump(standings.get_json(), outfile)
    return "Populated json_file..."


# def load_standings():
#     # with open('DataServerContainer/standings_dump.txt') as json_file:
#     #     current_standings = json.load(json_file)
#     # db.update_db(current_standings)
#     # db.db.insert(current_standings)
#     return "Standings updated in the database..."


get_standings_task = PythonOperator(
    task_id='get_standings',
    python_callable=get_standings,
    dag=standings_dag
)

# load_standings_task = PythonOperator(
#     task_id='load_standings',
#     python_callable=load_standings,
#     dag=standings_dag
# )

load_standings_task = BashOperator(
    task_id='load_standings',
    bash_command='curl --header "Content-Type: application/json" --request POST --data @./standings_dump.json http://127.0.0.1:4321/db/update',
    dag='standings_dag'
)

# cleanup = BashOperator(
#     task_id='cleanup_files',
#     bash_command='rm DataServerContainer/*.txt',
#     dag='standings_dag'
# )


get_standings_task >> load_standings_task
