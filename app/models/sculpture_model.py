from app.extentions import db


class Sculpture(db.Model):
    __tablename__ = 'sculptures'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    work_of_art_id = db.Column(db.Integer, db.ForeignKey('works_of_art.id', ondelete='CASCADE'))
    material = db.Column(db.String(100))
    weight = db.Column(db.Numeric(10, 2))
    work_of_art = db.relationship('WorkOfArt', backref=db.backref('sculptures', uselist=False, cascade="all, delete"))