from app.extentions import db


class VisitaGuiada(db.Model):
    __tablename__ = 'Visitas_Guiadas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grupo = db.Column(db.String(255))
    data_visita = db.Column(db.Date)
    horario = db.Column(db.Time)
    guia_responsavel_id = db.Column(db.Integer, db.ForeignKey('Guias.id'))
    guia = db.relationship('Guia', backref=db.backref('visitas_guiadas', lazy=True))