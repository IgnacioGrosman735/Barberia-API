from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app = Flask(__name__)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

#Permitir solicitudes desde cualquier origen
CORS(app)

# Rutas
#app.route('/', methods = ['GET'])(index)
#app.route('/probar_base', methods = ['POST'])(testear_base)

# Rutas para el CRUD de la entidad Movie
app.route('/', methods=['GET'])(index)
app.route('/api/turnos/', methods=['POST'])(create_turno)
app.route('/api/turnos/', methods=['GET'])(get_all_turnos)
"""app.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)
app.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
app.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie) """

if __name__ == '__main__':
    app.run(debug=True)