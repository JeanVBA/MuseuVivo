from app.extentions import db


class Ingresso(db.Model):
    __tablename__ = 'Ingressos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitante_id = db.Column(db.Integer, db.ForeignKey('Visitantes.id'))
    tipo = db.Column(db.String(50))
    data_visita = db.Column(db.Date)
    visita_guiada_id = db.Column(db.Integer, db.ForeignKey('Visitas_Guiadas.id'))
    visitante = db.relationship('Visitante', backref=db.backref('ingressos', lazy=True))
    visita_guiada = db.relationship('VisitaGuiada', backref=db.backref('ingressos', lazy=True))