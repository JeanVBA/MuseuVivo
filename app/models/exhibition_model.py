from app.extentions import db


class Exhibition(db.Model):
    __tablename__ = 'exhibitions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    exhibition_works_of_art = db.relationship('ExhibitionWorkOfArt', back_populates='exhibition', cascade="all, delete-orphan")
