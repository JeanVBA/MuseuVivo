from app.repositories.base_repository import BaseRepository
from app.models.location_model import Location


class LocationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Location)

    def get_by_name(self, name):
        return Location.query.filter_by(name=name).first()
