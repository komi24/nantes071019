# -*- coding: utf-8 -*-
from functools import wraps
from flask import Flask, render_template, request, redirect

from models import db
from models.Task import Task


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.sqlite3"

with app.app_context():
    db.init_app(app)
    db.create_all()


def isAuthenticated(f):
    @wraps(f)
    def nouvelle_fonction():
        if request.form.get("token") == "tsqjfnsdjgnSDJKgnw":
            return f()
        else:
            return error()
    return nouvelle_fonction

def ensureMozilla(f):
    @wraps(f)
    def nouvelle_fonction():
        print("headers", request.headers)
        return f()
    return nouvelle_fonction

@app.route("/")
@ensureMozilla
def home():
    liste_de_taches = Task.query.all()
    return render_template("index.html", ma_liste=liste_de_taches)

@app.route("/form", methods=["POST"])
@isAuthenticated
@ensureMozilla
def form():
    # Création d'une nouvelle tache
    task = Task(text=request.form.get("task"))
    db.session.add(task)
    db.session.commit()
    # Récupérer toutes les taches dans la db
    liste_de_taches = Task.query.all()
    return render_template("index.html", ma_liste=liste_de_taches)


@app.route("/delete/<idx>")
def delete(idx):
    # Supprimer la tache idx
    task = Task.query.get(idx)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/not-mozilla")
def error():
    return "Erreur"

app.run(port=5000, debug=True)
