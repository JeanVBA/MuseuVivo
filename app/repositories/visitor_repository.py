from app.repositories.base_repository import BaseRepository
from app.models.visitor_model import Visitor


class VisitorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Visitor)

    def get_by_args(self, name=None, email=None, phone=None):
        query = Visitor.query
        if name:
            query = query.filter(Visitor.name.ilike(f'%{name}%'))
        if email:
            query = query.filter(Visitor.email.ilike(f'%{email}%'))
        if phone:
            query = query.filter(Visitor.phone.ilike(f'%{phone}%'))
        return query.all()
    def get_by_name(self, name):
        return Visitor.query.filter_by(name=name).first()
