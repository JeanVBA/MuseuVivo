from app.models.work_of_art_model import WorkOfArt
from app.services.base_service import BaseService
from app.repositories.sculpture_repository import SculptureRepository


class SculptureService(BaseService):
    def __init__(self):
        super().__init__(SculptureRepository())

    def to_dict(self, sculpture):
        return {
            'id': sculpture.id,
            'work_of_art_id': sculpture.work_of_art_id,
            'material': sculpture.material,
            'weight': sculpture.weight,
            'work_of_art': {
                'id': sculpture.work_of_art.id,
                'name': sculpture.work_of_art.name,
                'description': sculpture.work_of_art.description,
                'creation_date': sculpture.work_of_art.creation_date,
                'author': sculpture.work_of_art.author.name if sculpture.work_of_art.author else None,
                'location': sculpture.work_of_art.location.name if sculpture.work_of_art.location else None,
                'type': sculpture.work_of_art.type
            }
        }

    def create(self, data):
        sculpture_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'material': data.get('material'),
            'weight': data.get('weight')
        }
        if sculpture_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having associated a work", 400)
        work_of_art = WorkOfArt.query.get(sculpture_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if work_of_art.type != 'Sculpture':
            return self.error_response("To register a sculpture, the work of art must be of the 'Sculpture' type.", 400)
        if sculpture_data['material'] is None:
            return self.error_response("Cannot be registered without material", 400)
        if sculpture_data['weight'] is None:
            return self.error_response("Cannot be registered without weight", 400)
        instance = self.repository.create(**sculpture_data)
        return self.to_dict(instance)

    def update(self, sculpture_id, data):
        sculpture = self.repository.get_by_id(sculpture_id)
        if sculpture is None:
            return self.error_response("Sculpture not found", 404)
        sculpture_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'material': data.get('material'),
            'weight': data.get('weight')
        }
        if sculpture_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having associated a work", 400)
        work_of_art = WorkOfArt.query.get(sculpture_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if work_of_art.type != 'Sculpture':
            return self.error_response("To register a sculpture, the work of art must be of the 'Sculpture' type.", 400)
        if sculpture_data['material'] is None:
            return self.error_response("Cannot be registered without material", 400)
        if sculpture_data['weight'] is None:
            return self.error_response("Cannot be registered without weight", 400)
        instance = self.repository.update(sculpture, **sculpture_data)
        return self.to_dict(instance)

    def fetch_by_id(self, sculpture_id):
        try:
            instance = self.repository.get_by_id(sculpture_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Sculpture not found", 404)

    def delete(self, sculpture_id):
        try:
            instance = self.repository.query.get(sculpture_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Sculpture not found", 404)

    def fetch_by_work_of_art_name(self, work_of_art_name):
        return [self.to_dict(instance) for instance in self.repository.get_by_work_of_art_name(work_of_art_name)]

    def fetch_by_args(self, work_of_art_name=None, material=None, weight=None):
        results = self.repository.get_by_args(work_of_art_name, material, weight)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
