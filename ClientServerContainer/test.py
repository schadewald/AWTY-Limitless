import requests
import pandas as pd

# getting schedule
r = requests.get(
    "http://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2020/league/00_full_schedule.json")
schedule_json = r.json()
df = pd.json_normalize(schedule_json, record_path=['lscd', 'mscd', 'g'])
# print(df.columns.values)

schedule = df[['gid', 'gdte', 'v.tn', 'h.tn']]
print(schedule.head())
