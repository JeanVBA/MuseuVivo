from app.repositories.base_repository import BaseRepository
from app.models.security_model import Security


class SecurityRepository(BaseRepository):
    def __init__(self):
        super().__init__(Security)

    def get_by_args(self, name=None, email=None, phone=None, location_nome=None):
        query = Security.query
        if name:
            query = query.filter(Security.name.ilike(f'%{name}%'))
        if email:
            query = query.filter(Security.email.ilike(f'%{email}%'))
        if phone:
            query = query.filter(Security.phone == phone)
        if location_nome:
            query = query.filter(Security.location.name.ilike(f'%{location_nome}%'))
        return query.all()
    def get_by_name(self, name):
        return Security.query.filter_by(name=name).first()
