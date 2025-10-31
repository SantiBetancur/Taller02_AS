import json
import os
import random


def load_pokeneas()-> dir:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'pokeneas.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data['pokeneas']

def get_random_pokenea() -> dir:
    data = load_pokeneas()
    return random.choice(data)