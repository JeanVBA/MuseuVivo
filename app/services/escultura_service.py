from app.models.obra_model import Obra
from app.services.base_service import BaseService
from app.repositories.escultura_repository import EsculturaRepository


class EsculturaService(BaseService):
    def __init__(self):
        super().__init__(EsculturaRepository())

    def to_dict(self, escultura):
        return {
            'id': escultura.id,
            'obra_id': escultura.obra_id,
            'material': escultura.material,
            'peso': escultura.peso,
            'obra': {
                'id': escultura.obra.id,
                'nome': escultura.obra.nome,
                'descricao': escultura.obra.descricao,
                'data_criacao': escultura.obra.data_criacao,
                'autor': escultura.obra.autor.nome if escultura.obra.autor else None,
                'localizacao': escultura.obra.localizacao.nome if escultura.obra.localizacao else None,
                'tipo': escultura.obra.tipo
            }
        }

    def create(self, data):
        escultura_data = {
            'obra_id': data.get('obra_id'),
            'material': data.get('material'),
            'peso': data.get('peso')
        }
        if escultura_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(escultura_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if obra.tipo != 'Escultura':
            return self.error_response("Para cadastrar escultura, é necessario que a obra seja do tipo 'Escultura'.", 400)
        if escultura_data['material'] is None:
            return self.error_response("Não pode ser cadastrado sem mateiral", 400)
        if escultura_data['peso'] is None:
            return self.error_response("Não pode ser cadastrado sem material", 400)
        instance = self.repository.create(**escultura_data)
        return self.to_dict(instance)

    def update(self, id, data):
        escultura = self.repository.get_by_id(id)
        escultura_data = {
            'obra_id': data.get('obra_id'),
            'material': data.get('material'),
            'peso': data.get('peso')
        }
        if escultura_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(escultura_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if escultura_data['material'] is None:
            return self.error_response("Não pode ser cadastrado sem mateiral", 400)
        if escultura_data['peso'] is None:
            return self.error_response("Não pode ser cadastrado sem material", 400)
        instance = self.repository.update(escultura, **escultura_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            instance = self.repository.get_by_id(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Escultura não encontrada", 404)

    def delete(self, id):
        try:
            instance = self.repository.query.get(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Escultura não encontrada", 404)

    def fetch_by_obra_nome(self, obra_nome):
        return [self.to_dict(instance) for instance in self.repository.get_by_obra_nome(obra_nome)]