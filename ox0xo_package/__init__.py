from flask import render_template
from CTFd.models import db

class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(64))
    name = db.Column(db.String(64))

    def __init__(self, image, name):
        self.image = image
        self.name = name


def load(app):
    app.db.create_all()
    @app.route("/faq", methods=["GET"])
    def view_faq():
        return render_template("page.html", content="<h1>FAQ Page<h1>")

