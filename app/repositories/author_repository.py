from app.repositories.base_repository import BaseRepository
from app.models.author_model import Autor


class AutorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Autor)

    def get_by_name(self, nome):
        return Autor.query.filter_by(nome=nome).first()

    def get_by_args(self, autor_id=None, nome=None):
        query = Autor.query
        if id:
            query = query.filter(Autor.id == autor_id)
        if nome:
            query = query.filter(Autor.nome.ilike(f'%{nome}%'))
        return query.all()