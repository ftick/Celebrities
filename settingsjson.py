import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Setup instructions'},
    {'type': 'bool',
     'title': 'Custom Cards',
     'desc': 'Play with custom cards or an existing set of cards',
     'section': 'example',
     'key': 'boolexample'},
    {'type': 'options',
     'title': 'Round timer',
     'desc': 'Duration of each round',
     'section': 'example',
     'key': 'timer_options',
     'options': ['30 sec', '1 min', '2 min']},
    {'type': 'options',
     'title': 'Number of Rounds',
     'desc': 'Number of rounds for the game',
     'section': 'example',
     'key': 'round_options',
     'options': ['3', '5', '7']},
    ])
