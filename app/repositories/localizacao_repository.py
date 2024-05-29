from app.repositories.base_repository import BaseRepository
from app.models.localizacao_model import Localizacao


class LocalizacaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Localizacao)
