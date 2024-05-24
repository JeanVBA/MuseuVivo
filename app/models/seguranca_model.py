from app.extentions import db


class Seguranca(db.Model):
    __tablename__ = 'Segurancas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(20))
    localizacao_id = db.Column(db.Integer, db.ForeignKey('Localizacoes.id'))
    localizacao = db.relationship('Localizacao', backref=db.backref('segurancas', lazy=True))