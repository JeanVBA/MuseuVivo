from flask import Flask
from app.extentions import db, migrate
from app.config import Config
from app.routes import (autor_route, emprestimo_route, obra_route, instituicao_route, obraExposicao_route,
                        exposicao_route, guia_route, visitante_route, seguranca_route, localizacao_route,
                        escultura_route, pintura_route, ingresso_route, visitaGuiada_route)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(autor_route.autor_bp)
    app.register_blueprint(emprestimo_route.emprestimo_bp)
    app.register_blueprint(obra_route.obra_bp)
    app.register_blueprint(instituicao_route.instituicao_bp)
    app.register_blueprint(obraExposicao_route.obraExposicao_bp)
    app.register_blueprint(exposicao_route.exposicao_bp)
    app.register_blueprint(guia_route.guia_bp)
    app.register_blueprint(visitante_route.visitante_bp)
    app.register_blueprint(seguranca_route.seguranca_bp)
    app.register_blueprint(localizacao_route.localizacao_bp)
    app.register_blueprint(escultura_route.escultura_bp)
    app.register_blueprint(pintura_route.pintura_bp)
    app.register_blueprint(ingresso_route.ingresso_bp)
    app.register_blueprint(visitaGuiada_route.visitaGuiada_bp)

    return app
