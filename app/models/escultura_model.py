from app.extentions import db


class Escultura(db.Model):
    __tablename__ = 'Esculturas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obra_id = db.Column(db.Integer, db.ForeignKey('Obras.id', ondelete='CASCADE'))
    material = db.Column(db.String(100))
    peso = db.Column(db.Numeric(10, 2))
    obra = db.relationship('Obra', backref=db.backref('escultura', uselist=False, cascade="all, delete"))