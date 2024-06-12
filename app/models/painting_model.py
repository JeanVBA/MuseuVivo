from app.extentions import db

class Painting(db.Model):
    __tablename__ = 'paintings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    work_of_art_id = db.Column(db.Integer, db.ForeignKey('works_of_art.id', ondelete='CASCADE'))
    technique = db.Column(db.String(100))
    work_of_art = db.relationship('WorkOfArt', backref=db.backref('painting', uselist=False, cascade="all, delete"))