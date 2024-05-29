import re

from app.services.base_service import BaseService
from app.repositories.guia_repository import GuiaRepository
class GuiaService(BaseService):
    def __init__(self):
        super().__init__(GuiaRepository())

    def to_dict(self, guia):
        return {
            'id': guia.id,
            'nome': guia.nome,
            'email': guia.email,
            'telefone': guia.telefone
        }

    def create(self, data):
        guia_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
        }
        if  guia_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if guia_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if guia_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if guia_data['email'] and not re.match(self.email_regex, guia_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if guia_data['telefone'] and not re.match(self.telefone_regex, guia_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.create(**guia_data)
        return self.to_dict(instance)

    def update(self, id, data):
        guia = self.repository.get_by_id(id)
        guia_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
        }
        if guia_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if guia_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if guia_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if guia_data['email'] and not re.match(self.email_regex, guia_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if guia_data['telefone'] and not re.match(self.telefone_regex, guia_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.update(guia, **guia_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            data = self.repository.get_by_id(id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Guia não encontrado", 404)

    def delete(self, id):
        try:
            data = self.repository.get_by_id(id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Guia não encontrado", 404)