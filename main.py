import json

from core import run_game

if __name__ == '__main__':
    configuration = json.load(open('config.json', 'r'))
    print(configuration)
    run_game(configuration)
