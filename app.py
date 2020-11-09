from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Players

@app.route('/')
def home():
    return "<h1>Welcome to EPL API</h1>"

@app.route("/add", methods=['POST'])
def add_player():
    name=request.args.get('name')
    club = request.args.get('club')
    age = request.args.get('age')
    nationality = request.args.get('nationality')
    appearances = request.args.get('appearances')
    goals = request.args.get('goals')
    assists = request.args.get('assists')
    player=Players(
        name=name,
        club=club,
        age=age,
        nationality=nationality,
        appearances=appearances,
        goals=goals,
        assists=assists
    )
    db.session.add(player)
    db.session.commit()
    return "Player added. player id={}".format(player.player_id)

@app.route("/getall")
def get_players():
    try:
        players=Players.query.all()
        return  jsonify([e.serialize() for e in players])
    except Exception as e:
	    return(str(e))


@app.route("/get/<player_id>")
def get_by_id(player_id):
    try:
        players=Players.query.filter_by(player_id=player_id).first()
        return jsonify(players.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/delete/<player_id>",methods=['DELETE'])
def delete_players(player_id):
    Players.query.filter_by(player_id=player_id).delete()
    db.session.commit()
    return  jsonify({"result":True})

if __name__ == '__main__':
    app.run()