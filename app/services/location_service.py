from app.services.base_service import BaseService
from app.repositories.location_repository import LocationRepository


class LocationService(BaseService):
    def __init__(self):
        super().__init__(LocationRepository())

    def to_dict(self, location):
        return {
            'id': location.id,
            'name': location.name,
        }

    def create(self, data):
        name = data.get('name')
        if not name:
            return self.error_response("Name field must be filled in", 400)
        instance = self.repository.create(name=name)
        return self.to_dict(instance)

    def update(self, location_id, data):
        location = self.repository.get_by_id(location_id)
        name = data.get('name')
        if not name:
            return self.error_response("Name field must be filled in", 400)
        autor = self.repository.update(location, name=name)
        return self.to_dict(autor)

    def fetch_by_id(self, location_id):
        try:
            location = self.repository.get_by_id(location_id)
            return self.to_dict(location)
        except Exception as e:
            return self.error_response("Location not found", 404)

    def delete(self, location_id):
        try:
            location = self.repository.get_by_id(location_id)
            self.repository.delete(location)
        except Exception as e:
            return self.error_response("Location not found", 404)

    def fetch_by_name(self, name):
        try:
            location = self.repository.get_by_name(name)
            return self.to_dict(location)
        except Exception as e:
            return self.error_response("Location not found", 404)
