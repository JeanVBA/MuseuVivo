from app.extentions import db

class Obra(db.Model):
    __tablename__ = 'Obras'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.Date)
    autor_id = db.Column(db.Integer, db.ForeignKey('Autores.id'))
    localizacao_id = db.Column(db.Integer, db.ForeignKey('Localizacoes.id'))
    tipo = db.Column(db.String(50))
    autor = db.relationship('Autor', backref=db.backref('obras', lazy=True))
    localizacao = db.relationship('Localizacao', backref=db.backref('obras', lazy=True))
    obras_exposicoes = db.relationship('ObraExposicao', back_populates='obra')
