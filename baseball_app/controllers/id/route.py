import logging

from flask import request, render_template
from pybaseball import playerid_lookup

from app import settings
from app.main import app


@app.route('/top')
def top():
    return render_template('common/top.html')



@app.route('/player_search', methods=['GET', 'POST'])
def input_player_name():
    if request.method == 'POST':
        player_name_first = request.form.get('player_name_first').strip()
        player_name_last = request.form.get('player_name_last').strip()
        player_data = playerid_lookup(player_name_last, player_name_first)
        player_key_mlbam = player_data['key_mlbam']
        if player_key_mlbam.values[0]:
            player_id = player_key_mlbam.values[0]
            return render_template('id/show_player_id.html', player_id=player_id)
        logging.warn('')

    return render_template('id/input_player_name.html', app_name=settings.APP_NAME)