from app.extentions import db

class WorkOfArt(db.Model):
    __tablename__ = 'works_of_art'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    creation_date = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    type = db.Column(db.String(10))
    author = db.relationship('Author', backref=db.backref('works_of_art', lazy=True))
    location = db.relationship('Location', backref=db.backref('works_of_art', lazy=True))
    works_of_art_exhibitions = db.relationship('ExhibitionWorkOfArt', back_populates='work_of_art')
