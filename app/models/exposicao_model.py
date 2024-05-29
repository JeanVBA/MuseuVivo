from app.extentions import db

class Exposicao(db.Model):
    __tablename__ = 'Exposicoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)
    obras_exposicoes = db.relationship('ObraExposicao', back_populates='exposicao')