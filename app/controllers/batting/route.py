import logging
from crypt import methods

from flask import Flask, request, render_template

from pybaseball import playerid_lookup, statcast_batter

import settings



app = Flask(__name__, template_folder='../../../templates', static_folder='../../../static')

class WebServer:
    def start(self, debug):
        app.run(host='0.0.0.0', port=settings.PORT, debug=debug)

server = WebServer()

APP_NAME = 'PlayViz'


@app.route('/top')
def top():
    return render_template('top.html')



@app.route('/player_search', methods=['GET', 'POST'])
def input_player_name():
    if request.method == 'POST':
        player_name_first = request.form.get('player_name_first').strip()
        player_name_last = request.form.get('player_name_last').strip()
        player_data = playerid_lookup(player_name_last, player_name_first)
        player_key_mlbam = player_data['key_mlbam']
        if player_key_mlbam.values[0]:
            player_id = player_key_mlbam.values[0]
            return render_template('show_player_id.html', player_id=player_id)
        logging.warn('')

    return render_template('input_player_name.html', app_name=APP_NAME)