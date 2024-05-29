import re

from app.models.localizacao_model import Localizacao
from app.services.base_service import BaseService
from app.repositories.seguranca_repository import SegurancaRepository
class SegurancaService(BaseService):
    def __init__(self):
        super().__init__(SegurancaRepository())

    def to_dict(self, seguranca):
        return {
            'id': seguranca.id,
            'nome': seguranca.nome,
            'email': seguranca.email,
            'telefone': seguranca.telefone,
            'localizacao': seguranca.localizacao.nome,
        }

    def create(self, data):
        seguranca_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
            'localizacao_id': data.get('localizacao_id'),
        }
        if seguranca_data['localizacao_id'] is None:
            return self.error_response("Necessario localizacao alocada", 400)
        localizacao = Localizacao.query.get(seguranca_data['localizacao_id'])
        if localizacao is None:
            return self.error_response("Localização não encontrada", 400)
        if  seguranca_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if seguranca_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if seguranca_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if seguranca_data['email'] and not re.match(self.email_regex, seguranca_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if seguranca_data['telefone'] and not re.match(self.telefone_regex, seguranca_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.create(**seguranca_data)
        return self.to_dict(instance)

    def update(self, id, data):
        seguranca = self.repository.get_by_id(id)
        seguranca_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
            'localizacao_id': data.get('localizacao_id'),
        }
        if seguranca_data['localizacao_id'] is None:
            return self.error_response("Necessario localizacao alocada", 400)
        localizacao = Localizacao.query.get(seguranca_data['localizacao_id'])
        if localizacao is None:
            return self.error_response("Localização não encontrada", 400)
        if seguranca_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if seguranca_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if seguranca_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if seguranca_data['email'] and not re.match(self.email_regex, seguranca_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if seguranca_data['telefone'] and not re.match(self.telefone_regex, seguranca_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.update(seguranca, **seguranca_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            data = self.repository.get_by_id(id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Seguranca não encontrado", 404)

    def delete(self, id):
        try:
            data = self.repository.get_by_id(id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Seguranca não encontrado", 404)