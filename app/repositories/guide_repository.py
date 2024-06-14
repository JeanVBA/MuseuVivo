from app.repositories.base_repository import BaseRepository
from app.models.guide_model import Guide


class GuideRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guide)

    def get_by_args(self, name=None,email=None,phone=None):
        query = Guide.query
        if name:
            query = query.filter(Guide.name.ilike(f'%{name}%'))
        if email:
            query = query.filter(Guide.email.ilike(f'%{email}%'))
        if phone:
            query = query.filter(Guide.phone.ilike(f'%{phone}%'))
        return query.all()
    def get_by_name(self, name):
        return Guide.query.filter_by(name=name).first()
