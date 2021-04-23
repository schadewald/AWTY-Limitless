import requests
import pandas as pd
import datetime

response = requests.get("http://nbadb:4321/db/retrieve")
print("queried API")
standings_json = response.json()
standings = pd.json_normalize(
    standings_json, record_path=['0', 'Standings'])
df_cleaned_standings = standings[['TeamName', 'Record']]

print(df_cleaned_standings.head())
print(datetime.date.today())
