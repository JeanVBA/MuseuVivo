from app.models.author_model import Author
from app.models.exhibition_model import Exhibition
from app.models.location_model import Location
from app.repositories.base_repository import BaseRepository
from app.models.work_of_art_model import WorkOfArt


class WorkOfArtRepository(BaseRepository):
    def __init__(self):
        super().__init__(WorkOfArt)

    def get_by_args(self, name=None, creation_date=None, author_name=None, location_name=None,
                    work_of_art_type=None):
        query = WorkOfArt.query
        if name:
            query = query.filter(WorkOfArt.name.ilike(f'%{name}%'))
        if author_name:
            query = query.join(Author).filter(Author.name.ilike(f'%{author_name}%'))
        if creation_date:
            query = query.filter(WorkOfArt.creation_date == creation_date)
        if location_name:
            query = query.join(Location).filter(Location.name.ilike(f'%{location_name}%'))
        if work_of_art_type:
            query = query.filter(WorkOfArt.type.ilike(f'%{work_of_art_type}%'))
        return query.all()
