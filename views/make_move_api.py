from storage import games
from flask import request


def make_move():
    game_id, player_key = request.form['game_id'], request.form['player_key']
    board = request.form['board']

    if game_id not in games.keys():
        return 'error'

    if games[game_id].player1_key == player_key:
        player = 1
    elif games[game_id].player2_key == player_key:
        player = 2
    else:
        return 'error'

    if games[game_id].current_move != player:
        return 'error'

    return games[game_id].make_move(board)
