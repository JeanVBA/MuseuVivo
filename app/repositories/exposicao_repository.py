from app.repositories.base_repository import BaseRepository
from app.models.exposicao_model import Exposicao


class ExposicaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Exposicao)
