from app.repositories.base_repository import BaseRepository
from app.models.pintura_model import Pintura


class PinturaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Pintura)
