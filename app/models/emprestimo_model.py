from app.extentions import db

class Emprestimo(db.Model):
    __tablename__ = 'Emprestimos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obra_id = db.Column(db.Integer, db.ForeignKey('Obras.id'))
    instituicao_id = db.Column(db.Integer, db.ForeignKey('Instituicoes.id'))
    data_emprestimo = db.Column(db.Date)
    data_retorno = db.Column(db.Date)
    obra = db.relationship('Obra', backref='emprestimos')