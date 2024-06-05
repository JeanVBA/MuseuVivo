from app.models.guia_model import Guia
from app.models.visitante_model import Visitante
from app.repositories.base_repository import BaseRepository
from app.models.ingresso_model import Ingresso


class IngressoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ingresso)

    def get_by_args(self, tipo=None, visitante_nome=None):
        query = Ingresso.query
        if tipo:
            query = query.filter(Ingresso.tipo.ilike(f'%{tipo}%'))
        if visitante_nome:
            query = query.join(Visitante).filter(Visitante.nome.ilike(f'%{visitante_nome}%'))
        return query.all()

    def get_by_type(self, tipo):
        return Ingresso.query.filter_by(tipo=tipo).all()
