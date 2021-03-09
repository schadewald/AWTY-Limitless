from nba_api.stats.endpoints import leaguestandings
import json

standings = leaguestandings.LeagueStandings(season='2020-21')
# df_standings = standings.get_data_frames()[0]  #standings in table form
standings = standings.get_normalized_json()
json_object = json.loads(standings)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)