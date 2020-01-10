import json

from flask import request

from storage import games, Game
from random import randint


def create_game():
    size_of_board, length_of_win_comb = int(request.form['size_of_board']), int(request.form['length_of_win_comb'])
    game = Game(game_id=str(len(games) + 1), player1_key=str(randint(0, 100000)),
                size_of_board=size_of_board, length_of_win_comb=length_of_win_comb)
    games[game.id] = game
    resp = json.dumps({'game_id': game.id, 'player_key': game.player1_key})
    return resp
