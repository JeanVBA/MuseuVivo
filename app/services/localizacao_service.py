from app.services.base_service import BaseService
from app.repositories.localizacao_repository import LocalizacaoRepository

class LocalizacaoService(BaseService):
    def __init__(self):
        super().__init__(LocalizacaoRepository())

    def to_dict(self, localizacao):
        return {
            'id': localizacao.id,
            'nome': localizacao.nome,
        }

    def create(self, data):
        nome = data.get('nome')
        if not nome:
            return self.error_response("Campo nome deve ser preenchido", 400)
        instance = self.repository.create(nome=nome)
        return self.to_dict(instance)

    def update(self, id, data):
        localizacao = self.repository.get_by_id(id)
        nome = data.get('nome')
        if not nome:
            return self.error_response("Campo nome deve ser preenchido", 400)
        autor = self.repository.update(localizacao, nome=nome)
        return self.to_dict(autor)

    def fetch_by_id(self, id):
        try:
            localizacao = self.repository.get_by_id(id)
            return self.to_dict(localizacao)
        except Exception as e:
            return self.error_response("Localizacao não encontrada", 404)

    def delete(self, id):
        try:
            localizacao = self.repository.get_by_id(id)
            self.repository.delete(localizacao)
        except Exception as e:
            return self.error_response("Localizacao não encontrada", 404)