from app.repositories.base_repository import BaseRepository
from app.models.escultura_model import Escultura


class EsculturaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Escultura)
