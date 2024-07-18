from flask import Flask
from flask_cors import CORS, cross_origin
from app.database import init_app
from app.views import *

app = Flask(__name__)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

#Permitir solicitudes desde cualquier origen
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Rutas
#app.route('/', methods = ['GET'])(index)
#app.route('/probar_base', methods = ['POST'])(testear_base)

# Rutas para el CRUD de la entidad Turnos
app.route('/', methods=['GET'])(index)
app.route('/api/turnos', methods=['POST'])(create_turno)
app.route('/api/turnos', methods=['GET'])(get_all_turnos)
app.route('/api/turnos/<int:id_turno>', methods=['GET'])(get_turno)
app.route('/api/turnos/<int:id_turno>', methods=['PUT'])(update_turno)
app.route('/api/turnos/<int:id_turno>', methods=['DELETE'])(delete_turno)

if __name__ == '__main__':
    app.run(debug=True)