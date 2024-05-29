from app.repositories.base_repository import BaseRepository
from app.models.visitante_model import Visitante


class VisitanteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Visitante)
