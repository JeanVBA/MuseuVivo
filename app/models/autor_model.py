from app.extentions import db


class Autor(db.Model):
    __tablename__ = 'Autores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)