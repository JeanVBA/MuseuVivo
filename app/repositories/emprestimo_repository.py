from app.models.instituicao_model import Instituicao
from app.repositories.base_repository import BaseRepository
from app.models.emprestimo_model import Emprestimo


class EmprestimoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Emprestimo)

    def get_by_instituicao_nome(self, instituicao_nome):
        return Emprestimo.query.join(Emprestimo.instituicao).filter(Instituicao.nome == instituicao_nome).all()