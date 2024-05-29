from app.extentions import db

class ObraExposicao(db.Model):
    __tablename__ = 'Obras_Exposicoes'
    obra_id = db.Column(db.Integer, db.ForeignKey('Obras.id'), primary_key=True)
    exposicao_id = db.Column(db.Integer, db.ForeignKey('Exposicoes.id'), primary_key=True)
    obra = db.relationship('Obra', back_populates='obras_exposicoes')
    exposicao = db.relationship('Exposicao', back_populates='obras_exposicoes')