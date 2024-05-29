from app.repositories.base_repository import BaseRepository
from app.models.seguranca_model import Seguranca


class SegurancaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Seguranca)
