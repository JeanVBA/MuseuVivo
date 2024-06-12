from app.repositories.base_repository import BaseRepository
from app.models.location_model import Localizacao


class LocalizacaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Localizacao)

    def get_by_name(self, nome):
        return Localizacao.query.filter_by(nome=nome).first()