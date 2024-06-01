from app.repositories.base_repository import BaseRepository
from app.models.visitante_model import Visitante


class VisitanteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Visitante)

    def get_by_name(self, nome):
        return Visitante.query.filter_by(nome=nome).first()