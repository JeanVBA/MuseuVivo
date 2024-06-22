from flask import jsonify

from app.models.author_model import Author
from app.models.location_model import Location
from app.models.work_of_art_model import WorkOfArt
from app.services.base_service import BaseService
from app.repositories.work_of_art_repository import WorkOfArtRepository


class WorkOfArtService(BaseService):
    def __init__(self):
        super().__init__(WorkOfArtRepository())

    def to_dict(self, work_of_art):
        work_of_art_dict = {
            'id': work_of_art.id,
            'name': work_of_art.name,
            'description': work_of_art.description,
            'creation_date': work_of_art.creation_date,
            'author': work_of_art.author.name if work_of_art.author else None,
            'location': work_of_art.location.name if work_of_art.location else None,
            'type': work_of_art.type
        }
        if work_of_art.type == 'Sculpture' and work_of_art.sculptures:
            sculpture = work_of_art.sculptures  # assuming one-to-one for simplicity
            work_of_art_dict['sculpture'] = {
                'material': sculpture.material,
                'weight': sculpture.weight
            }
        elif work_of_art.type == 'Painting' and work_of_art.painting:
            painting = work_of_art.painting  # assuming one-to-one for simplicity
            work_of_art_dict['painting'] = {
                'technique': painting.technique
            }
        return work_of_art_dict

    def create(self, data):
        work_of_art_data = {
            'name': data.get('name'),
            'description': data.get('description'),
            'creation_date': data.get('creation_date'),
            'author_id': data['author_id'],
            'location_id': data['location_id'],
            'type': data.get('type')
        }
        if work_of_art_data['type'] not in ['Sculpture', 'Painting']:
            return self.error_response('Type not found, please enter valid types "Sculpture or Painting".', 400)
        if work_of_art_data['author_id'] is None or not Author.query.get(work_of_art_data['author_id']):
            return self.error_response("Author not found", 400)
        if work_of_art_data['location_id'] is None or not Location.query.get(work_of_art_data['location_id']):
            return self.error_response("Location not found", 400)
        instance = self.repository.create(**work_of_art_data)
        return self.to_dict(instance)

    def update(self, work_of_art_id, data):
        work_of_art = self.repository.get_by_id(work_of_art_id)
        if work_of_art is None:
             return self.error_response("Work of art not found", 404)
        work_of_art_data = {
            'name': data.get('name'),
            'description': data.get('description'),
            'creation_date': data.get('creation_date'),
            'author_id': data['author_id'],
            'location_id': data['location_id'],
            'type': data.get('type')
        }
        if work_of_art_data['type'] not in ['Sculpture', 'Painting']:
            return self.error_response('Type not found, please enter valid types "Sculpture or Painting".', 400)
        if work_of_art_data['author_id'] is None or not Author.query.get(work_of_art_data['author_id']):
            return self.error_response("Author not found", 400)
        if work_of_art_data['location_id'] is None or not Location.query.get(work_of_art_data['location_id']):
            return self.error_response("Location not found", 400)
        work_of_art = self.repository.update(work_of_art, **work_of_art_data)
        return self.to_dict(work_of_art)

    def fetch_by_id(self, work_of_art_id):
        try:
            work_of_art = self.repository.get_by_id(work_of_art_id)
            return self.to_dict(work_of_art)
        except Exception as e:
            return self.error_response("Work of art not found", 404)

    def delete(self, work_of_art_id):
        try:
            work_of_art = self.repository.get_by_id(work_of_art_id)
            self.repository.delete(work_of_art)
        except Exception as e:
            return self.error_response("Work of art not found", 404)

    def fetch_by_args(self, name=None, creation_date=None, author_name=None, location_name=None, type=None):
        results = self.repository.get_by_args(name, creation_date, author_name, location_name, type)
        if results is None:
            return self.error_response("Cannot be registered without having a visitor associated", 404)
        return [self.to_dict(result) for result in results]


def work_of_art_to_dict(work_of_art):
    if work_of_art is None:
            return {}
    work_of_art_dict = {
        'name': work_of_art.name,
        'description': work_of_art.description,
        'creation_date': work_of_art.creation_date,
        'author': work_of_art.author.name if work_of_art.author else None,
        'type': work_of_art.type
    }
    if work_of_art.type == 'Sculpture' and work_of_art.sculptures:
        sculpture = work_of_art.sculptures  # assuming one-to-one for simplicity
        work_of_art_dict['sculpture'] = {
            'material': sculpture.material,
            'weight': sculpture.weight
        }
    elif work_of_art.type == 'Painting' and work_of_art.painting:
            painting = work_of_art.painting  # assuming one-to-one for simplicity
            work_of_art_dict['painting'] = {
                'technique': painting.technique
            }
    return work_of_art_dict
