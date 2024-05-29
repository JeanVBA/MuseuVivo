from app.models.obra_model import Obra
from app.services.base_service import BaseService
from app.repositories.pintura_repository import PinturaRepository


class PinturaService(BaseService):
    def __init__(self):
        super().__init__(PinturaRepository())

    def to_dict(self, pintura):
        return dict(id=pintura.id, obra_id=pintura.obra_id, tecnica=pintura.tecnica, obra={
            'id': pintura.obra.id,
            'nome': pintura.obra.nome,
            'descricao': pintura.obra.descricao,
            'data_criacao': pintura.obra.data_criacao,
            'autor': pintura.obra.autor.nome if pintura.obra.autor else None,
            'localizacao': pintura.obra.localizacao.nome if pintura.obra.localizacao else None,
        })

    def create(self, data):
        pintura_data = {
            'obra_id': data.get('obra_id'),
            'tecnica': data.get('tecnica')
        }
        if pintura_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(pintura_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if obra.tipo != 'Pintura':
            return self.error_response("Para cadastrar pintura, é necessario que a obra seja do tipo 'Pintura'.", 400)
        if pintura_data['tecnica'] is None:
            return self.error_response("Não pode ser cadastrado sem tecnica", 400)
        instance = self.repository.create(**pintura_data)
        return self.to_dict(instance)

    def update(self, id, data):
        pintura = self.repository.get_by_id(id)
        pintura_data = {
            'obra_id': data.get('obra_id'),
            'tecnica': data.get('tecnica')
        }
        if pintura_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(pintura_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if obra.tipo != 'Pintura':
            return self.error_response("Para cadastrar pintura, é necessario que a obra seja do tipo 'Pintura'.", 400)
        if pintura_data['tecnica'] is None:
            return self.error_response("Não pode ser cadastrado sem tecnica", 400)
        instance = self.repository.update(pintura, **pintura_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            instance = self.repository.get_by_id(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Pintura não encontrada", 404)

    def delete(self, id):
        try:
            instance = self.repository.query.get(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Pintura não encontrada", 404)
