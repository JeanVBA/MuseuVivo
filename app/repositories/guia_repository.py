from app.repositories.base_repository import BaseRepository
from app.models.guia_model import Guia


class GuiaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guia)

    def get_by_name(self, nome):
        return Guia.query.filter_by(nome=nome).first()