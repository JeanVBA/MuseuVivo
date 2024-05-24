from app.extentions import db

class Pintura(db.Model):
    __tablename__ = 'Pinturas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obra_id = db.Column(db.Integer, db.ForeignKey('Obras.id', ondelete='CASCADE'))
    tecnica = db.Column(db.String(100))
    obra = db.relationship('Obra', backref=db.backref('pintura', uselist=False, cascade="all, delete"))