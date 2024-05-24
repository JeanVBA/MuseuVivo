from app.extentions import db


class Localizacao(db.Model):
    __tablename__ = 'Localizacoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
