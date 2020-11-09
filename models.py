from app import db

class Players(db.Model):

    player_id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    club = db.Column(db.String(120))
    age= db.Column(db.Integer)
    nationality=db.Column(db.String(120))
    appearances=db.Column(db.Integer)
    goals=db.Column(db.Integer)
    assists=db.Column(db.Integer)

    def __init__(self, name, club, age,nationality,appearances,goals,assists):
        self.name = name
        self.club=club
        self.age=age
        self.nationality=nationality
        self.appearances=appearances
        self.goals=goals
        self.assists=assists

    def __repr__(self):
        return f"('{self.name}', '{self.club}', '{self.age}','{self.nationality}','{self.appearances}','{self.goals}','{self.assists})"

    def serialize(self):
        return {
            'player_id': self.player_id,
            'name': self.name,
            'club':self.club,
            'age':self.age,
            'nationality':self.nationality,
            'appearances':self.appearances,
            'goals':self.goals,
            'assists':self.assists
        }