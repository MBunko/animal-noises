from application import app
from flask import request, Response
import random 

@app.route('/animal', methods=["GET"])
def get_animal():
    animals = ["cow", "pig", "horse"]
    return Response(str(random.choice(animals)), mimetype='text/plain')

@app.route('/noise', methods=["POST"])
def get_noise():
    noises = {"cow":"moo", "pig":"oink", "horse":"neigh"}
    animal = request.get_json()
    return Response(noises[animal["animal"]], mimetype='text/plain')