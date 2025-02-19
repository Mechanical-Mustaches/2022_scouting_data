import json
from pprint import pprint
import os
from typing import Tuple, Any
import statistics

print('Congrats line 5 ran')

matches = []
regional = {}

class Team:
    def __init__(self):
        self.climbs = []
        self.shots_high = []
        self.taxis = []
        self.total_shots = []

    @property
    def shots_in_regional(self):
        return sum(self.shots_high)

    @property
    def shot_percentage(self):
        return round(self.shots_in_regional / sum(self.total_shots), 2)

    @property
    def climb_average(self):
        return statistics.mean(self.climbs)

    def fill_buckets(self, match: dict):
        # team = regional[match['team']]
        self.total_shots.append(match['total_shots'])
        self.climbs.append(match['climb'])
        self.shots_high.append(match['shot_high'])
        self.taxis.append(match['taxi'])




def shots_in_launch(launch: dict[any]) -> int:
    total_shots = 0
    # launch = match['t_shots'][0]
    shot_type = ['high_made', 'high_missed', 'low_made', 'low_missed']
    for shot in shot_type:
        total_shots = launch[shot] + total_shots
    return total_shots

def load_match(file: str) -> dict:
    with open(file, 'r') as f:
        smatch = f.read()

    # print(smatch)
    replace = {
        'meta_scouter_id': 'scouter',
        'meta_scout_time': 'time',
        'meta_scouting_duration': 'dur',
        'meta_scout_mode': 'mode',
        'meta_position': 'tarmac_pos',
        'meta_event_id': 'event',
        'meta_match': 'match',
        'meta_team': 'team',
        'match_auto_shooting': 'a_shots',
        'match_auto_other_taxi': 'taxi',
        'match_teleop_shooting': 't_shots',
        'match_teleop_climb_level': 'climb',
        'match_teleop_other_played_defense': 'defense',
        'match_post_notes_notes': 'notes',
        'match_post_notes_broke_down': 'broke_down',
        'match_post_notes_driver_skill': 'driver_skill',
        'a_shots_high_hub_made': 'high_made',
        'a_shots_high_hub_missed': 'high_missed',
        'a_shots_low_hub_made': 'low_made',
        'a_shots_low_hub_missed': 'low_missed',
        'a_shots_location': 'shot_location',
        't_shots_high_hub_made': 'high_made',
        't_shots_high_hub_missed': 'high_missed',
        't_shots_low_hub_made': 'low_made',
        't_shots_low_hub_missed': 'low_missed',
        't_shots_location': 'shots_location',
        't_shots_defended': 'shots_defended'
    }
    for key, value in replace.items():
        smatch = smatch.replace(key, value)
    match = json.loads(smatch)
    return match

def shots_in_match(launches):
    return sum([shots_in_launch(launch) for launch in launches])

def shots_made(launches): #returns the total high made
    # print(launch['high_made'])
    return sum([launch['high_made'] for launch in launches])

def match_data(_match) -> dict:
    return {
        'total_shots': shots_in_match(_match['t_shots']),
        'shot_high': shots_made(_match['t_shots']),
        'taxi': _match['taxi'],
        'climb': _match['climb'],
        'team': _match['team']
    }





def shot_percentage(team: int, matches):
    total = 0
    total_made = 0
    for each_match in matches:
        if each_match['team'] == team:
            total = total + each_match['total_shots']
            total_made = total_made + each_match['shot_high']
    return total_made/total, total, total_made


print('__name__ is ', __name__)




def load_folder(folder):
    global matches
    global regional
    all_match_files = os.listdir(folder)

    for each_match_file in all_match_files:
        if each_match_file[:5] == 'match':
            match = load_match(folder + '\\' + each_match_file)
            matches.append(match_data(match))

    #begin regional creation
    team_list = {match['team'] for match in matches}

    regional = {team: Team() for team in team_list}
    # regional = new_func(regional, matches)
    for match in matches:
        # team = regional[match['team']]
        # team.fill_buckets()
        regional[match['team']].fill_buckets(match)
    return matches, regional

# def fill_buckets():
#     global matches
#     global regional
#
#     for match in matches:
#
#         team.total_shots.append(match['total_shots'])
#         team.climbs.append(match['climb'])
#         team.shots_high.append(match['shot_high'])
#         team.taxis.append(match['taxi'])


    # return regional

if __name__ == '__main__':
    print('starting parse')

    matches, regional = load_folder('Midwest Regional')

    pprint(regional[111])
    pprint(matches[:3])

#which team had most total shots?
#which team highest shooting percentage?
#which team highest taxi percentage?
    # m = {'team': {'total_shots': 0, 'shooting_percent': 0, 'total_made': 0, 'shots': [0,1,2,3], 'taxi_percent': 0, 'climb': 'max_climb', 'climb_accuracy': 0, 'climbs': [1,2,3]}}
    # m[8122]['climb']

