from flask import Flask
from app.extentions import db, migrate
from app.config import Config
from app.controllers import (autor_controller, obra_controller, pintura_controller, escultura_controller,
                             localizacao_controller, emprestimo_controller, exposicao_controller)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(autor_controller.autor_bp)
    app.register_blueprint(localizacao_controller.localizacao_bp)
    app.register_blueprint(obra_controller.obra_bp)
    app.register_blueprint(escultura_controller.escultura_bp)
    app.register_blueprint(pintura_controller.pintura_bp)
    app.register_blueprint(emprestimo_controller.emprestimo_bp)
    app.register_blueprint(exposicao_controller.exposicao_bp)

    return app
