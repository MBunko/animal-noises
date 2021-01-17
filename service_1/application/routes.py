from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    animal_response = requests.get("http://animal-backend:5000/animal")
    noise_response = requests.post("http://animal-backend:5000/noise", data=animal_response.text)
    return render_template("index.html", animal=animal_response.text, noise=noise_response.text)