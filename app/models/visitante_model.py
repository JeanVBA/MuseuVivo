from app.extentions import db

class Visitante(db.Model):
    __tablename__ = 'Visitantes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(20))