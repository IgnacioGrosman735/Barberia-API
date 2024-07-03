from flask import jsonify, request
#from app.database import get_db
from app.models import Turno

""" def index():
    return jsonify({"mensaje": "Soy una api nuevita"}), 200

def testear_base():
    try:
        get_db()
        return jsonify({"Mensaje": "La conexión es un éxito"}), 200
    except BaseException as be:
        return jsonify({"Mensaje": "La conexión no funciona"}), 500 """


def index():
    return jsonify({'message': 'Hello World API Turnos'})

def create_turno():
    data = request.json
    new_turno = Turno(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], email=data['email'], dia=data['dia'])
    new_turno.save()
    return jsonify({'message': 'Turno creado'}), 201

def get_all_turnos():
    turnos = Turno.get_all()
    return jsonify([turno.serialize() for turno in turnos])