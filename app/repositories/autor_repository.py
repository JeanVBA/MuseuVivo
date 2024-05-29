from app.repositories.base_repository import BaseRepository
from app.models.autor_model import Autor


class AutorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Autor)
