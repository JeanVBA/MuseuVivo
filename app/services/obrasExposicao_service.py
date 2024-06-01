from app.models.exposicao_model import Exposicao
from app.models.obra_model import Obra
from app.services.base_service import BaseService
from app.services.obra_service import obra_to_dict
from app.services.exposicao_service import exposicao_to_dict
from app.repositories.obraExposicao_repository import ObraExposicaoRepository


class ObraExposicaoService(BaseService):
    def __init__(self):
        super().__init__(ObraExposicaoRepository())

    def to_dict(self, instance):
        return {
            'obra_id': instance.obra_id,
            'obra_nome': instance.obra.nome,
            'exposicao_id': instance.exposicao_id if instance.exposicao_id else None,
            'exposicao_titulo': instance.exposicao.titulo if instance.exposicao.titulo else None,
        }

    def exposicoes_to_dict(self, instance):
        return {
            'exposicao_id': instance.exposicao_id,
            'exposicao_titulo': instance.exposicao.titulo,
            'obras': [obra_to_dict(obra_exposicao.obra) for obra_exposicao in instance.exposicao.obras_exposicoes]
        }

    def obras_to_dict(self, instance):
        return {
            'obra_id': instance.obra_id,
            'obra_nome': instance.obra.nome,
            'exposicoes': [exposicao_to_dict(obra_exposicao.exposicao) for obra_exposicao in
                           instance.obra.obras_exposicoes]
        }

    def create(self, data):
        obra_id = data.get('obra_id')
        exposicao_id = data.get('exposicao_id')

        if obra_id is None or exposicao_id is None:
            return self.error_response("Obra ID e Exposição ID devem ser fornecidos", 400)
        obra = Obra.query.get(obra_id)
        if obra is None:
            return self.error_response("Obra não encontrada", 404)
        exposicao = Exposicao.query.get(exposicao_id)
        if exposicao is None:
            return self.error_response("Exposicao não encontrada", 404)

        instance = self.repository.create(obra_id=obra_id, exposicao_id=exposicao_id)
        return self.to_dict(instance)

    def update(self, obra_id, exposicao_id, data):
        obra_exposicao = self.repository.get_by_ids(obra_id, exposicao_id)
        if obra_exposicao is None:
            return self.error_response("Relacionamento não encontrado", 404)

        new_obra_id = data.get('obra_id')
        new_exposicao_id = data.get('exposicao_id')

        if new_obra_id is not None:
            obra = Obra.query.get(new_obra_id)
            if obra is None:
                return self.error_response("Obra não localizada", 404)
            obra_exposicao.obra_id = new_obra_id

        if new_exposicao_id is not None:
            exposicao = Exposicao.query.get(new_exposicao_id)
            if exposicao is None:
                return self.error_response("Exposição não localizada", 404)
            obra_exposicao.exposicao_id = new_exposicao_id

        instance = self.repository.update_by_ids(obra_exposicao)
        return self.to_dict(instance)

    def fetch_by_obra_id(self, obra_id):
        obra_exposicoes = self.repository.get_by_obra_id(obra_id)
        obras_set = set()
        unique_results = []
        for result in obra_exposicoes:
            if result.obra_id not in obras_set:
                obras_set.add(result.obra_id)
                unique_results.append(result)
        if not unique_results:
            return {"message": "No records found"}, 404
        if obra_exposicoes is not None:
            return [self.obras_to_dict(result) for result in unique_results]
        return self.error_response("Obra não encontrada", 404)

    def fetch_by_exposicao_id(self, exposicao_id):
        obra_exposicoes = self.repository.get_by_exposicao_id(exposicao_id)
        exposicoes_set = set()
        unique_results = []
        for result in obra_exposicoes:
            if result.exposicao_id not in exposicoes_set:
                exposicoes_set.add(result.exposicao_id)
                unique_results.append(result)
        if not unique_results:
            return {"message": "No records found"}, 404
        if obra_exposicoes is not None:
            return [self.exposicoes_to_dict(result) for result in unique_results]
        return self.error_response("Exposição não encontrada", 404)

    def delete(self, obra_id, exposicao_id):
        obra_exposicao = self.repository.get_by_ids(obra_id, exposicao_id)
        if obra_exposicao is None:
            return self.error_response("Relacionamento não encontrado", 404)
        self.repository.delete(obra_exposicao)
        return None
