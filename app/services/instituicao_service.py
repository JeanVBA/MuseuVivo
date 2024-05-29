from app.models.instituicao_model import Instituicao
from app.services.base_service import BaseService
from app.repositories.instituicao_repository import InstituicaoRepository
from app.services.obra_service import obra_to_dict

class InstituicaoService(BaseService):
    def __init__(self):
        super().__init__(InstituicaoRepository())

    def to_dict(self, instituicao):
        return {
            'id': instituicao.id,
            'nome': instituicao.nome,
            'obras': [obra_to_dict(emprestimo.obra) for emprestimo in instituicao.emprestimos]
        }

    def create(self, data):
        nome = data.get('nome')
        if nome is None:
            return self.error_response('Campo nome deve ser preenchido', 400)
        instance = self.repository.create(nome=nome)
        return self.to_dict(instance)

    def update(self, id, data):
        instituicao = self.repository.get_by_id(id)
        nome = data.get('nome')
        if nome is None:
            return self.error_response('Campo nome deve ser preenchido', 400)
        instance = self.repository.update(instituicao, nome=nome)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            instituicao = self.repository.get_by_id(id)
            return self.to_dict(instituicao)
        except Exception as e:
            return self.error_response("Instituicao não encontrada", 404)

    def delete(self, id):
        try:
            instituicao = self.repository.get_by_id(id)
            self.repository.delete(instituicao)
        except Exception as e:
            return self.error_response("Instituicao não encontrado", 404)