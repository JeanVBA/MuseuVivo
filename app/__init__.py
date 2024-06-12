from flask import Flask
from app.extentions import db, migrate
from app.config import Config
from app.routes import (author_route, loan_route, work_of_art_route, institution_route, exhibition_work_of_art_route,
                        exhibition_route, guide_route, visitor_route, security_route, location_route,
                        sculpture_route, painting_route, ticket_route, guided_visit_route)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(author_route.author_bp)
    app.register_blueprint(loan_route.loan_bp)
    app.register_blueprint(work_of_art_route.work_of_art_bp)
    app.register_blueprint(institution_route.institution_bp)
    app.register_blueprint(exhibition_work_of_art_route.exhibition_work_of_art_bp)
    app.register_blueprint(exhibition_route.exhibition_bp)
    app.register_blueprint(guide_route.guide_bp)
    app.register_blueprint(visitor_route.visitor_bp)
    app.register_blueprint(security_route.security_bp)
    app.register_blueprint(location_route.location_bp)
    app.register_blueprint(sculpture_route.sculpture_bp)
    app.register_blueprint(painting_route.painting_bp)
    app.register_blueprint(ticket_route.ticket_bp)
    app.register_blueprint(guided_visit_route.guided_visit_bp)

    return app
