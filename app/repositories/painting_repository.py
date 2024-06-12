from app.repositories.base_repository import BaseRepository
from app.models.painting_model import Painting


class PaintingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Painting)

    def get_by_args(self, work_of_art_name=None, technique=None):
        query = Painting.query
        if technique:
            query = query.filter(Painting.technique.ilike(f'%{technique}%'))
        if work_of_art_name:
            query = query.filter(Painting.work_of_art.name.ilike(f'%{work_of_art_name}%'))
        return query.all()
