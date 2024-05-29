from app.repositories.base_repository import BaseRepository
from app.models.obraExposicao_model import ObraExposicao


class ObraExposicaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(ObraExposicao)

    def get_by_obra_id(self, obra_id):
        return self.model.query.filter_by(obra_id=obra_id).all()

    def get_by_exposicao_id(self, exposicao_id):
        return self.model.query.filter_by(exposicao_id=exposicao_id).all()