from app.repositories.base_repository import BaseRepository
from app.models.ingresso_model import Ingresso


class IngressoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ingresso)
