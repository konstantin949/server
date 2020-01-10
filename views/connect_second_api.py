import json
from flask import request
from storage import games
from random import randint


def connect_second_player():
    game_id = request.form['game_id']
    c = games
    x = games[game_id].player2_key

    if games[game_id].player2_key is not None:
        return 'error'

    games[game_id].player2_key = str(randint(0, 100000))
    resp = json.dumps({'player_key': games[game_id].player2_key})
    return resp

