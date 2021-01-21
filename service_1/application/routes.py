from application import app, db
from flask import render_template
from sqlalchemy import desc
import requests
from os import getenv

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)
    animal_noise = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    animal_response = requests.get("http://animal-noises_animal-backend:5000/animal")
    noise_response = requests.post("http://animal-noises_animal-backend:5000/noise", json={"animal" : animal_response.text})
 
    db.session.add(Animals(
        animal_type = animal_response.text, 
        animal_noise = noise_response.text
    ))
    db.session.commit()

    all_animals = Animals.query.order_by(desc("id")).limit(5).all()

    return render_template("index.html", 
        animal=animal_response.text,
        noise=noise_response.text,
        all_animals=all_animals,
        app_version=getenv("APP_VERSION")
    )