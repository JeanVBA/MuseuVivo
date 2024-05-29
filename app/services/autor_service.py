from app.services.base_service import BaseService
from app.repositories.autor_repository import AutorRepository

class AutorService(BaseService):
    def __init__(self):
        super().__init__(AutorRepository())

    def to_dict(self, autor):
        return {
            'id': autor.id,
            'nome': autor.nome,
        }

    def create(self, data):
        nome = data.get('nome')
        if not nome:
            return self.error_response("Campo nome deve ser preenchido", 400)
        instance = self.repository.create(nome=nome)
        return self.to_dict(instance)

    def update(self, id, data):
        autor = self.repository.get_by_id(id)
        nome = data.get('nome')
        if not nome:
            return self.error_response("Campo nome deve ser preenchido", 400)
        autor = self.repository.update(autor, nome=nome)
        return self.to_dict(autor)

    def fetch_by_id(self, id):
        try:
            autor = self.repository.get_by_id(id)
            return self.to_dict(autor)
        except Exception as e:
            return self.error_response("Autor não encontrado", 404)

    def delete(self, id):
        try:
            autor = self.repository.get_by_id(id)
            self.repository.delete(autor)
        except Exception as e:
            return self.error_response("Autor não encontrado", 404)