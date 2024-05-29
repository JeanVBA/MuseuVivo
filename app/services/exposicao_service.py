from datetime import datetime

from app.services.base_service import BaseService
from app.repositories.exposicao_repository import ExposicaoRepository

class ExposicaoService(BaseService):
    def __init__(self):
        super().__init__(ExposicaoRepository())

    def to_dict(self,exposicao):
        return {
            'exposicao_id': exposicao.id,
            'titulo': exposicao.titulo,
            'descricao': exposicao.descricao,
            'data_inicio': exposicao.data_inicio,
            'data_termino': exposicao.data_termino
        }

    def create(self, data):
        exposicao_data = {
            'titulo': data.get('titulo'),
            'descricao': data.get('descricao'),
            'data_inicio': data.get('data_inicio'),
            'data_termino': data['data_termino']
        }
        if exposicao_data['titulo'] is None:
            return self.error_response("Titulo não pode ser nulo", 400)
        if exposicao_data['data_termino'] and datetime.fromisoformat(exposicao_data['data_termino']) < datetime.now():
            return self.error_response("A data do termino não pode ser antes da data atual", 400)
        instance = self.repository.create(**exposicao_data)
        return self.to_dict(instance)

    def update(self, id, data):
        exposicao = self.repository.get_by_id(id)
        exposicao_data = {
            'titulo': data.get('titulo'),
            'descricao': data.get('descricao'),
            'data_inicio': data.get('data_inicio'),
            'data_termino': data['data_termino']
        }
        if exposicao_data['titulo'] is None:
            return self.error_response("Titulo não pode ser nulo", 400)
        if exposicao_data['data_termino'] and datetime.fromisoformat(exposicao_data['data_termino']) < datetime.now():
            return self.error_response("A data do termino não pode ser antes da data atual", 400)
        autor = self.repository.update(exposicao, **exposicao_data)
        return self.to_dict(autor)

    def fetch_by_id(self, id):
        try:
            exposicao = self.repository.get_by_id(id)
            return self.to_dict(exposicao)
        except Exception as e:
            return self.error_response("Exposicao não encontrado", 404)

    def delete(self, id):
        try:
            exposicao = self.repository.get_by_id(id)
            self.repository.delete(exposicao)
        except Exception as e:
            return self.error_response("Exposicao não encontrado", 404)

def exposicao_to_dict(exposicao):
    return {
        'titulo': exposicao.titulo,
        'descricao': exposicao.descricao,
        'data_inicio': exposicao.data_inicio,
        'data_termino': exposicao.data_termino
    }