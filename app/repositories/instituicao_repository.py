from app.repositories.base_repository import BaseRepository
from app.models.instituicao_model import Instituicao


class InstituicaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Instituicao)
