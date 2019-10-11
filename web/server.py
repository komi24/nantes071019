# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

liste_de_taches = [
    "Invitez-les à faire des cours dans notre merveilleuse ville",
    "Faites une partie de molky",
    "Il ne pleut pas",
    "Dire que la plage n'est pas loin (mentir)",
]


@app.route("/")
def home():
    return render_template("index.html", ma_liste=liste_de_taches)


@app.route("/form", methods=["POST"])
def form():
    liste_de_taches.append(request.form.get("task"))
    return render_template("index.html", ma_liste=liste_de_taches)


app.run(port=5000, debug=True)
