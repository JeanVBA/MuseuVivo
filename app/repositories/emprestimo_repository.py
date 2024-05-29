from app.repositories.base_repository import BaseRepository
from app.models.emprestimo_model import Emprestimo


class EmprestimoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Emprestimo)
