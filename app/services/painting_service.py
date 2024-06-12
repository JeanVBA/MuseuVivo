from app.models.work_of_art_model import WorkOfArt
from app.services.base_service import BaseService
from app.repositories.painting_repository import PaintingRepository


class PaintingService(BaseService):
    def __init__(self):
        super().__init__(PaintingRepository())

    def to_dict(self, painting):
        return dict(id=painting.id, work_of_art_id=painting.work_of_art_id, technique=painting.technique,
                    work_of_art={
                        'id': painting.work_of_art.id,
                        'name': painting.work_of_art.name,
                        'description': painting.work_of_art.description,
                        'creation_date': painting.work_of_art.creation_date,
                        'author': painting.work_of_art.author.name if painting.work_of_art.author else None,
                        'location': painting.work_of_art.location.name if painting.work_of_art.location else None,
                        }
                    )

    def create(self, data):
        painting_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'technique': data.get('technique')
        }
        if painting_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having a Work of art associated", 400)
        work_of_art = WorkOfArt.query.get(painting_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if work_of_art.type != 'Painting':
            return self.error_response("To register a painting, the work must be of the type 'Painting'.", 400)
        if painting_data['technique'] is None:
            return self.error_response("Technique field must be filled in", 400)
        instance = self.repository.create(**painting_data)
        return self.to_dict(instance)

    def update(self, painting_id, data):
        painting = self.repository.get_by_id(painting_id)
        painting_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'technique': data.get('technique')
        }
        if painting_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having a Work of art associated", 400)
        work_of_art = WorkOfArt.query.get(painting_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if work_of_art.type != 'Painting':
            return self.error_response("To register a painting, the work must be of the type 'Painting'.", 400)
        if painting_data['technique'] is None:
            return self.error_response("Technique field must be filled in", 400)
        instance = self.repository.update(painting, **painting_data)
        return self.to_dict(instance)

    def fetch_by_id(self, painting_id):
        try:
            instance = self.repository.get_by_id(painting_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Painting not found", 404)

    def delete(self, painting_id):
        try:
            instance = self.repository.query.get(painting_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Painting not found", 404)

    def fetch_by_args(self, work_of_art_name=None, technique=None):
        results = self.repository.get_by_args(work_of_art_name, technique)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]