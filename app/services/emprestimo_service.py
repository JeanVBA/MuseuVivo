from app.models.instituicao_model import Instituicao
from app.models.obra_model import Obra
from app.services.base_service import BaseService
from app.repositories.emprestimo_repository import EmprestimoRepository
from datetime import datetime


class EmprestimoService(BaseService):
    def __init__(self):
        super().__init__(EmprestimoRepository())

    def to_dict(self, emprestimo):
        return {
            'id': emprestimo.id,
            'obra': {
                'id': emprestimo.obra.id,
                'nome': emprestimo.obra.nome,
                'descricao': emprestimo.obra.descricao,
                'data_criacao': emprestimo.obra.data_criacao,
                'autor': emprestimo.obra.autor.nome if emprestimo.obra.autor else None,
                'localizacao': emprestimo.obra.localizacao.nome if emprestimo.obra.localizacao else None,
                'tipo': emprestimo.obra.tipo
            },
            'data_emprestimo': emprestimo.data_emprestimo,
            'data_retorno': emprestimo.data_retorno,
            'instituicao': emprestimo.instituicao.nome,
        }
    def create(self, data):
        emprestimo_data = {
            'obra_id': data.get('obra_id'),
            'data_emprestimo': data.get('data_emprestimo'),
            'data_retorno': data.get('data_retorno'),
            'instituicao_id': data.get('instituicao_id')
        }
        if emprestimo_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(emprestimo_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if emprestimo_data['data_retorno'] and datetime.fromisoformat(emprestimo_data['data_retorno']) < datetime.now():
            return self.error_response("A data do retorno não pode ser antes da data atual", 400)
        if emprestimo_data['instituicao_id'] is None:
            return self.error_response("Instituicao deve ser preenchida", 400)
        instituicao = Instituicao.query.get(emprestimo_data['instituicao_id'])
        if instituicao is None:
            return self.error_response("Obra não localizada", 404)
        instance = self.repository.create(**emprestimo_data)
        return self.to_dict(instance)

    def update(self, id, data):
        emprestimo = self.repository.get_by_id(id)
        emprestimo_data = {
            'obra_id': data.get('obra_id'),
            'data_emprestimo': data.get('data_emprestimo'),
            'data_retorno': data.get('data_retorno'),
            'instituicao_id': data.get('instituicao_id')
        }
        if emprestimo_data['obra_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
        obra = Obra.query.get(emprestimo_data['obra_id'])
        if obra is None:
            return self.error_response("Obra não localizada", 404)
        if emprestimo_data['data_retorno'] and datetime.fromisoformat(emprestimo_data['data_retorno']) < datetime.now():
            return self.error_response("A data do retorno não pode ser antes da data atual", 400)
        if emprestimo_data['instituicao_id'] is None:
            return self.error_response("Instituicao deve ser preenchida", 400)
        instituicao = Instituicao.query.get(emprestimo_data['instituicao_id'])
        if instituicao is None:
            return self.error_response("Instituicao não localizada", 404)
        emprestimo = self.repository.update(emprestimo, **emprestimo_data)
        return self.to_dict(emprestimo)

    def fetch_by_id(self, id):
        try:
            emprestimo = self.repository.get_by_id(id)
            return self.to_dict(emprestimo)
        except Exception as e:
            return self.error_response("Emprestimo não encontrado", 404)

    def delete(self, id):
        try:
            emprestimo = self.repository.query.get(id)
            return self.to_dict(emprestimo)
        except Exception as e:
            return self.error_response("Emprestimo não encontrado", 404)
