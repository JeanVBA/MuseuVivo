from app.models.work_of_art_model import WorkOfArt
from app.repositories.base_repository import BaseRepository
from app.models.sculpture_model import Sculpture


class SculptureRepository(BaseRepository):
    def __init__(self):
        super().__init__(Sculpture)

    def get_by_args(self, work_of_art_name=None, material=None, weight=None):
        query = Sculpture.query
        if material:
            query = query.filter(Sculpture.material == material)
        if weight:
            query = query.filter(Sculpture.weight == weight)
        if work_of_art_name:
            query = query.filter(Sculpture.work_of_art.name.ilike(f'%{work_of_art_name}%'))
        return query.all()
    def get_by_work_of_art_name(self, work_of_art_name):
        return Sculpture.query.join(Sculpture.work_of_art).filter(WorkOfArt.name == work_of_art_name).all()
