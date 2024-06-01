import re

from app.services.base_service import BaseService
from app.repositories.visitante_repository import VisitanteRepository
class VisitanteService(BaseService):
    def __init__(self):
        super().__init__(VisitanteRepository())

    def to_dict(self, visitante):
        return {
            'id': visitante.id,
            'nome': visitante.nome,
            'email': visitante.email,
            'telefone': visitante.telefone
        }

    def create(self, data):
        visitante_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
        }
        if  visitante_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if visitante_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if visitante_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if visitante_data['email'] and not re.match(self.email_regex, visitante_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if visitante_data['telefone'] and not re.match(self.telefone_regex, visitante_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.create(**visitante_data)
        return self.to_dict(instance)

    def update(self, id, data):
        guia = self.repository.get_by_id(id)
        visitante_data = {
            'nome': data.get('nome'),
            'email': data.get('email'),
            'telefone': data.get('telefone'),
        }
        if visitante_data['nome'] is None:
            return self.error_response("Campo nome deve ser preenchido", 400)
        if visitante_data['email'] is None:
            return self.error_response("Campo email deve ser preenchido", 400)
        if visitante_data['telefone'] is None:
            return self.error_response("Campo telefone deve ser preenchido", 400)
        if visitante_data['email'] and not re.match(self.email_regex, visitante_data['email']):
            return self.error_response("Formato de email inválido", 400)
        if visitante_data['telefone'] and not re.match(self.telefone_regex, visitante_data['telefone']):
            return self.error_response("Formato de telefone inválido", 400)
        instance = self.repository.update(guia, **visitante_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            data = self.repository.get_by_id(id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Visitante não encontrado", 404)

    def delete(self, id):
        try:
            data = self.repository.get_by_id(id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Visitante não encontrado", 404)

    def fetch_by_name(self, nome):
        result = self.repository.get_by_name(nome)
        if result is not None:
            return self.to_dict(result)
        return self.error_response("Visitante não encontrado", 404)