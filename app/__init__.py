import os
from flask import Flask
from flask_marshmallow import Marshmallow
from app.Config import config
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app()->Flask:

    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f =  config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    ma.init_app(app)
    CORS(app)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.routes import categorias 
    app.register_blueprint(categorias)

    @app.shell_context_processor
    def ctx():
        return {"app": app}
    
    return app                