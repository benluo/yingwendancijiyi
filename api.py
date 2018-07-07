from flask import Flask
from flask_restful import Api
from models import db
from resources import *

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    api = Api(app)
    api.add_resource(WordListResource, '/words')
    api.add_resource(WordResource, '/words/<int:id>')
    api.add_resource(WordByEnWordResource, '/<string:enWord>')
    api.add_resource(QueryResource, '/q')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
