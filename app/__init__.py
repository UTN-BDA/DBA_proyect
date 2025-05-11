import os
from flask import Flask
from flask_marshmallow import Marsmallow
from app.Config import config
from flask_cors import CORS

ma=Marsmallow

def create_app()->Flask:

    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f =  config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    ma.init_app(app)
    CORS(app)

    #from app.Routes import ...
    #app.register_blueprint(...)

    @app.shell_context_processor
    def ctx():
        return {"app": app}
    
    return app                