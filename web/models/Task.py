from . import db

class Task(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	text=db.Column(db.String(100))
	