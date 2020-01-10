# -*- coding: utf-8 -*-
from flask import Flask
from views import create_game, connect_second_player, connected_second_player, can_i_move, make_move, get_list_of_games


app = Flask(__name__)


app.add_url_rule('/api/create_game', view_func=create_game, methods=['POST'])
app.add_url_rule('/api/connect_second_player', view_func=connect_second_player, methods=['POST'])
app.add_url_rule('/api/connected_second_player', view_func=connected_second_player, methods=['POST'])
app.add_url_rule('/api/can_i_move', view_func=can_i_move, methods=['POST'])
app.add_url_rule('/api/make_move', view_func=make_move, methods=['POST'])
app.add_url_rule('/api/get_list_of_games', view_func=get_list_of_games)


if __name__ == '__main__':
    app.run(threaded=True)
