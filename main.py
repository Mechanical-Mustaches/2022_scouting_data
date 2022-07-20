import json
from pprint import pprint


mary = """Do, do do do, do do do, do do do, do do do do do
Do, do do do, do do do, do do do, do do do do do
Mary had a little lamb
Little lamb, little lamb
Mary had a little lamb
It's fleece was white as snow
Everywhere that Mary went
Mary went, Mary went
Everywhere that Mary went
The lamb was sure to go
It followed her to school one day
School one day, school one day
It followed her to school one day
Which was against the rules"""

if __name__ == '__main__':
    print('starting parse')
    # string.replace(old, new, count)
    replace = {'do': 'turtle',
               'Do':'sea',
               'lamb':'fish',
               'fleece':'scales'}
    for key, value in replace.items():
        mary = mary.replace(key, value)

    pprint(mary)
    with open('match-2022ilch-45-8122.json', 'r') as f:
        smatch = f.read()

    print(smatch)
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
    pprint(match)