from app.models.autor_model import Autor
from app.models.localizacao_model import Localizacao
from app.models.obra_model import Obra
from app.services.base_service import BaseService
from app.repositories.obra_repository import ObraRepository

class ObraService(BaseService):
    def __init__(self):
        super().__init__(ObraRepository())

    def to_dict(self, obra):
        obra_dict = {
            'id': obra.id,
            'nome': obra.nome,
            'descricao': obra.descricao,
            'data_criacao': obra.data_criacao,
            'autor': obra.autor.nome if obra.autor else None,
            'localizacao': obra.localizacao.nome if obra.localizacao else None,
            'tipo': obra.tipo
        }
        if obra.tipo == 'Escultura' and obra.escultura:
            obra_dict['escultura'] = {
                'material': obra.escultura.material,
                'peso': obra.escultura.peso
            }
        elif obra.tipo == 'Pintura' and obra.pintura:
            obra_dict['pintura'] = {
                'tecnica': obra.pintura.tecnica
            }
        return obra_dict

    def create(self, data):
        obra_data = {
            'nome': data.get('nome'),
            'descricao': data.get('descricao'),
            'data_criacao': data.get('data_criacao'),
            'autor_id': data['autor_id'],
            'localizacao_id': data['localizacao_id'],
            'tipo': data.get('tipo')
        }
        if obra_data['tipo'] not in ['Escultura', 'Pintura']:
            return self.error_response('Tipo não encontrado, insira tipos válidos "Escultura ou Pintura".', 400)
        if obra_data['autor_id'] is None or not Autor.query.get(obra_data['autor_id']):
            return self.error_response("Autor não localizado.", 400)
        if obra_data['localizacao_id'] is None or not Localizacao.query.get(obra_data['localizacao_id']):
            return self.error_response("Localizacao inexistente", 400)
        instance = self.repository.create(**obra_data)
        return self.to_dict(instance)

    def update(self, id, data):
        obra_obj = self.repository.get_by_id(id)
        obra_data = {
            'nome': data.get('nome'),
            'descricao': data.get('descricao'),
            'data_criacao': data.get('data_criacao'),
            'autor_id': data['autor_id'],
            'localizacao_id': data['localizacao_id'],
            'tipo': data.get('tipo')
        }
        if obra_data['tipo'] not in ['Escultura', 'Pintura']:
            return self.error_response('Tipo não encontrado, insira tipos válidos "Escultura ou Pintura".', 400)
        if obra_data['autor_id'] is None or not Autor.query.get(obra_data['autor_id']):
            return self.error_response("Autor não localizado.", 400)
        if obra_data['localizacao_id'] is None or not Localizacao.query.get(obra_data['localizacao_id']):
            return self.error_response("Localizacao inexistente", 400)
        autor = self.repository.update(obra_obj, **obra_data)
        return self.to_dict(autor)

    def fetch_by_id(self, id):
        try:
            obra = self.repository.get_by_id(id)
            return self.to_dict(obra)
        except Exception as e:
            return self.error_response("Obra não encontrado", 404)

    def delete(self, id):
        try:
            obra = self.repository.get_by_id(id)
            self.repository.delete(obra)
        except Exception as e:
            return self.error_response("Obra não encontrado", 404)

def obra_to_dict(obra):
    obra_dict = {
        'nome': obra.nome,
        'descricao': obra.descricao,
        'data_criacao': obra.data_criacao,
        'autor': obra.autor.nome if obra.autor else None,
        'tipo': obra.tipo
    }
    if obra.tipo == 'Escultura' and obra.escultura:
        obra_dict['escultura'] = {
            'material': obra.escultura.material,
            'peso': obra.escultura.peso
        }
    elif obra.tipo == 'Pintura' and obra.pintura:
        obra_dict['pintura'] = {
            'tecnica': obra.pintura.tecnica
        }
    return obra_dict