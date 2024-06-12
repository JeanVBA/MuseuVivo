from app.extentions import db


class Instituicao(db.Model):
    __tablename__ = 'institutions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    loans = db.relationship('Loan', backref='institution', lazy=True)