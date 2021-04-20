import random
import pandas as pd
import requests


class MonteCarlo():
    def __init__(self):
        self.season = '2020-21'


def simGame(teamA, teamB, teamA_ELO, teamB_ELO):
    # random number from 0 to 1 to be compared to the win probability for team A
    toCompare = random.uniform(0, 1)
    elo_diff = teamA_ELO - teamB_ELO
    probA = 1 / (10**(-elo_diff/400) + 1)
    # if toCompare < probA:
    #     # teamA wins
    #     # increment teamA wins
    #     # increase teamA ELO, decrease teamB ELO
    # else:
    #     # teamB wins
    #     # increment teamB wins
    #     # increase team B ELO, decrease teamA ELO


# def simSeason():


# def updateELO(teamA_ELO, teamB_ELO):
#     # update ELO


def getELO():
    # from ELO collection ["team", "elo"]
    response = requests.get("http://nbadb:4321/db/retrieve/elo")

    elo_json = response.json()
    elo = pd.json_normalize(elo_json, record_path=['0'])

    return elo


def getStandings():
    # from NBA collection ["TeamName", "Record"]
    print("about to query API")
    response = requests.get("http://nbadb:4321/db/retrieve")
    print("queried API")
    standings_json = response.json()
    standings = pd.json_normalize(
        standings_json, record_path=['0', 'Standings'])
    df_cleaned_standings = standings[['TeamName', 'Record']]

    return df_cleaned_standings


def getSchedule():
    # from Schedule collection ["gdte", "vistor", "home"]
    response = requests.get("http://nbadb:4321/db/retrieve/schedule")

    schedule_json = response.json()
    schedule = pd.json_normalize(schedule_json, record_path=['0'])

    return schedule


print(getSchedule())
