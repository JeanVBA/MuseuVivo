from app.models.work_of_art_model import WorkOfArt
from app.repositories.base_repository import BaseRepository
from app.models.exhibition_model import Exhibition


class ExhibitionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Exhibition)

    def get_by_args(self, title=None, start_date=None, end_date=None):
        query = Exhibition.query
        if start_date:
            query = query.filter(Exhibition.start_date == start_date)
        if end_date:
            query = query.filter(Exhibition.end_date == end_date)
        if title:
            query = query.filter(Exhibition.title.ilike(f'%{title}%'))
        return query.all()
    def get_by_title(self, title):
        return Exhibition.query.filter_by(title=title).first()
