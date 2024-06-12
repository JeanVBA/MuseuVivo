from app.repositories.base_repository import BaseRepository
from app.models.institution_model import Institution


class InstituicaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Instituicao)

    def get_by_args(self, nome=None, emprestimo_nome=None, data_emprestimo=None, data_retorno_empestimo=None):
        query = Instituicao.query
        if nome:
            query = query.filter(Instituicao.nome.ilike(f'%{nome}%'))
        if emprestimo_nome:
            query = query.filter(Instituicao.emprestimo.nome.ilike(f'%{emprestimo_nome}%'))
        if data_retorno_empestimo:
            query = query.filter(Instituicao.emprestimo.data_retorno == data_retorno_empestimo)
        if data_emprestimo:
            query = query.filter(Instituicao.emprestimo.data_emprestimo == data_emprestimo)
        return query.all()
    def get_by_name(self, nome):
        return Instituicao.query.filter_by(nome=nome).first()