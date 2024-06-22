from app.extentions import db

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    work_of_art_id = db.Column(db.Integer, db.ForeignKey('works_of_art.id', ondelete='CASCADE'))
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id', ondelete='CASCADE'))
    loan_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    amount_collected = db.Column(db.Numeric(10, 2), nullable=False)
    work_of_art = db.relationship('WorkOfArt', back_populates='loans')
    institution = db.relationship('Institution', back_populates='loans')
