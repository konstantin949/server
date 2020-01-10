import time
import json
from storage import games
from flask import request


def connected_second_player():
    game_id = request.form['game_id']
    player1_key = request.form['player_key']

    if game_id not in games.keys() or games[game_id].player1_key != player1_key:
        return 'error'

    while True:
        if games[game_id].player2_key:
            return 'connected'
        time.sleep(0.5)


def can_i_move():
    game_id, player_key = request.form['game_id'], request.form['player_key']

    if game_id not in games.keys():
        return 'error'

    if games[game_id].player1_key == player_key:
        player = 1
    elif games[game_id].player2_key == player_key:
        player = 2
    else:
        return 'error'

    while True:
        if games[game_id].current_move == player and games[game_id].winner is None:
            return json.dumps({'board': games[game_id].board, 'winner': '-'})
        elif games[game_id].current_move == player and games[game_id].winner:
            return json.dumps({'board': games[game_id].board, 'winner': games[game_id].winner})
        time.sleep(0.5)


def get_list_of_games():
    list_of_games = []
    for game in games.keys():
        if games[game].player2_key is None:
            list_of_games.append({'game_id': games[game].id, 'size_of_board': games[game].size_of_board,
                                  'length_of_win_comb': games[game].length_of_win_comb})
    return json.dumps(list_of_games)





