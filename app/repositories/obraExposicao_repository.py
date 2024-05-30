from app import db
from app.repositories.base_repository import BaseRepository
from app.models.obraExposicao_model import ObraExposicao


class ObraExposicaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(ObraExposicao)

    def update_by_ids(self, instance):
        db.session.commit()
        return instance

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()

    def get_by_ids(self, obra_id, exposicao_id):
        return ObraExposicao.query.filter_by(obra_id=obra_id, exposicao_id=exposicao_id).first()

    def get_by_obra_id(self, obra_id):
        return self.model.query.filter_by(obra_id=obra_id).all()

    def get_by_exposicao_id(self, exposicao_id):
        return self.model.query.filter_by(exposicao_id=exposicao_id).all()