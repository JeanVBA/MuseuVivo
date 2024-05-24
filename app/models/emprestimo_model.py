from app.extentions import db

class Emprestimo(db.Model):
    __tablename__ = 'Emprestimos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obra_id = db.Column(db.Integer, db.ForeignKey('Obras.id'))
    data_emprestimo = db.Column(db.Date)
    data_retorno = db.Column(db.Date)
    instituicao_solicitante = db.Column(db.String(255))
    obra = db.relationship('Obra', backref=db.backref('emprestimos', lazy=True))