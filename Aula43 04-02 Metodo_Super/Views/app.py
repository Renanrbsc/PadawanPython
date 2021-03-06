import sys
sys.path.append(r'C:\Users\900159\Documents\GitHub\TrabalhosPython\Aula43 04-02 API_Pokemon')
sys.path.append(r'C:\Users\Usuario\Documents\GitHub\TrabalhosPython\Aula43 04-02')
from flask import Flask, render_template
from flask_restful import Api

from Controllers.treinador_controller import TreinadorController
from Controllers.pokemon_controller import PokemonController

app = Flask(__name__)
api = Api(app)

api.add_resource(TreinadorController, '/api/treinador', endpoint='treinadores')
api.add_resource(TreinadorController, '/api/treinador/<int:id>', endpoint='treinador')

api.add_resource(PokemonController, '/api/pokemon', endpoint='pokemons')
api.add_resource(PokemonController, '/api/pokemon/<int:id>', endpoint='pokemon')

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
