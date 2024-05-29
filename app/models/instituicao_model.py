from app.extentions import db


class Instituicao(db.Model):
    __tablename__ = 'Instituicoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    emprestimos = db.relationship('Emprestimo', backref='instituicao', lazy=True)