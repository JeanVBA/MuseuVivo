from app.repositories.base_repository import BaseRepository
from app.models.visitaGuiada_model import VisitaGuiada


class VisitaGuiadaRepository(BaseRepository):
    def __init__(self):
        super().__init__(VisitaGuiada)
