from app.repositories.base_repository import BaseRepository
from app.models.seguranca_model import Seguranca


class SegurancaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Seguranca)

    def get_by_name(self, nome):
        return Seguranca.query.filter_by(nome=nome).first()