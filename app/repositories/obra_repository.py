from app.repositories.base_repository import BaseRepository
from app.models.obra_model import Obra


class ObraRepository(BaseRepository):
    def __init__(self):
        super().__init__(Obra)
