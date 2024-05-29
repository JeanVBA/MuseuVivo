from app.repositories.base_repository import BaseRepository
from app.models.guia_model import Guia


class GuiaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guia)
