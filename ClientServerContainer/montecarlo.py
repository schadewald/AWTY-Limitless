import random
import pandas as pd
import requests
import numpy as np


class MonteCarlo():
    def __init__(self, num_sims):
        self.season = '2020-21'
        self.num_sims = num_sims
        self.getStandings()
        self.master_table = self.standings[['TeamName', 'Conference']].copy()
        self.master_table['num_playoffs'] = 0
        self.master_table['playoff_pct'] = 0

    def prepare(self):
        standings = self.getStandings()
        elo = self.getELO()

        # merge ELO and Standings
        standings_elo = pd.merge(
            standings, elo, left_on='TeamName', right_on='team', how='inner').drop(columns=['team'])
        # standings_elo = standings_elo.set_index('TeamName')
        return standings_elo

    def simGame(self, standings_elo):
        master = pd.DataFrame
        schedule = self.getSchedule()
        # get current days games and beyond
        # today = datetime.date.today()
        schedule = schedule[pd.to_datetime(
            schedule['gdte']) > pd.Timestamp('today').floor('D')]
        # print('starting simulation...')
        # print(standings_elo.head())
        # print(schedule.head())
        for idx, row in schedule.iterrows():
            teamA_name = row['home']
            #print(f'team A name: {teamA_name}')
            teamB_name = row['visitor']
            #print(f'team B name: {teamB_name}')
            teamA_filter = (standings_elo["TeamName"] == teamA_name)
            teamB_filter = (standings_elo["TeamName"] == teamB_name)

            teamA_elo = standings_elo.loc[standings_elo['TeamName']
                                          == teamA_name, 'elo']
            #print(f'team A ELO: {(teamA_elo.item())}')
            teamB_elo = standings_elo.loc[standings_elo['TeamName']
                                          == teamB_name, 'elo']
            #print(f'team B ELO: {teamB_elo.item()}')

            # SIM GAME
            # random number from 0 to 1 to be compared to the win probability for team A
            toCompare = random.uniform(0, 1)
            elo_diff = teamA_elo.item() - teamB_elo.item()
            probA = 1 / (10**(-elo_diff/400) + 1)
            #print('teamA win prob: {}'.format(probA))
            if toCompare < probA:
                # teamA wins
                # increment teamA wins
                # increment teamB losses
                standings_elo.loc[teamA_filter,
                                  'WINS'] = standings_elo['WINS'] + 1
                standings_elo.loc[teamB_filter,
                                  'LOSSES'] = standings_elo['LOSSES'] + 1
                # increase teamA ELO, decrease teamB ELO
                standings_elo.loc[teamA_filter,
                                  'elo'] = standings_elo['elo'] + 20
                standings_elo.loc[teamB_filter,
                                  'elo'] = standings_elo['elo'] - 20
            else:
                # teamB wins
                # increment teamB wins
                standings_elo.loc[teamB_filter,
                                  'WINS'] = standings_elo['WINS'] + 1
                standings_elo.loc[teamA_filter,
                                  'LOSSES'] = standings_elo['LOSSES'] + 1
                # increase teamA ELO, decrease teamB ELO
                standings_elo.loc[teamB_filter,
                                  'elo'] = standings_elo['elo'] + 20
                standings_elo.loc[teamA_filter,
                                  'elo'] = standings_elo['elo'] - 20
            # print('----------------------------')

        #print('...rest of season simulated...')
        # print(standings_elo)
        self.calcPlayoffProb(standings_elo)
        return standings_elo

    # def updateELO(teamA_ELO, teamB_ELO):
    #     # update ELO

    def calcPlayoffProb(self, standings_elo):
        # add 'made_playoffs' column: 1, 0
        grouped = standings_elo.groupby('Conference').apply(
            lambda x: x.sort_values(by='WINS', ascending=False))
        # print(grouped)
        west = grouped[grouped['Conference'] == 'West']
        west = west[:8]
       # print(west)
        east = grouped[grouped['Conference'] == 'East']
        east = east[:8]
       # print(east)
        playoff_teams = pd.concat([east, west])
        playoff_teams = list(playoff_teams['TeamName'])
        self.master_table.loc[self.master_table['TeamName'].isin(
            playoff_teams), 'num_playoffs'] += 1
        self.master_table['playoff_pct'] = self.master_table['num_playoffs'] / self.num_sims
        # print(self.master_table)

    def getELO(self):
        # from ELO collection ["team", "elo"]
        response = requests.get("http://nbadb:4321/db/retrieve/elo")

        elo_json = response.json()
        elo = pd.json_normalize(elo_json, record_path=['0', 'teams'])
        return elo

    def getStandings(self):
        # from NBA collection ["TeamName", "WINS", "LOSSES"]
        response = requests.get("http://nbadb:4321/db/retrieve")
        standings_json = response.json()
        self.standings = pd.json_normalize(
            standings_json, record_path=['0', 'Standings'])
        df_cleaned_standings = self.standings[[
            'TeamName', 'WINS', 'LOSSES', 'Conference']]

        return df_cleaned_standings

    def getSchedule(self):
        # from Schedule collection ["gdte", "vistor", "home"]
        # response = requests.get("http://nbadb:4321/db/retrieve/schedule")

        r = requests.get(
            "http://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2020/league/00_full_schedule.json")
        schedule_json = r.json()
        df = pd.json_normalize(schedule_json, record_path=[
                               'lscd', 'mscd', 'g'])
        # print(df.columns.values)

        schedule = df[['gid', 'gdte', 'v.tn', 'h.tn']]
        schedule = schedule.rename(columns={'v.tn': 'visitor', 'h.tn': 'home'})

        return schedule

    def print_master(self):
        print(self.master_table)


numSims = 10  # set to 10 simulations for testing purposes, runs slower as numSims increase
sim = MonteCarlo(numSims)
df = sim.prepare()
for i in range(sim.num_sims):
    sim.simGame(df)
sim.print_master()
