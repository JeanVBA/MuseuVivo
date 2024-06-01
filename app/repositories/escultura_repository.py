from app.models.obra_model import Obra
from app.repositories.base_repository import BaseRepository
from app.models.escultura_model import Escultura


class EsculturaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Escultura)

    def get_by_obra_nome(self, obra_nome):
        return Escultura.query.join(Escultura.obra).filter(Obra.nome == obra_nome).all()