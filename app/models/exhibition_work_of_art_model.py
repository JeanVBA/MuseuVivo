from app.extentions import db


class ExhibitionWorkOfArt(db.Model):
    __tablename__ = 'works_of_art_exhibitions'
    work_of_art_id = db.Column(db.Integer, db.ForeignKey('works_of_art.id', ondelete='CASCADE'), primary_key=True)
    exhibition_id = db.Column(db.Integer, db.ForeignKey('exhibitions.id', ondelete='CASCADE'), primary_key=True)
    work_of_art = db.relationship('WorkOfArt', back_populates='exhibition_works_of_art')
    exhibition = db.relationship('Exhibition', back_populates='exhibition_works_of_art')
