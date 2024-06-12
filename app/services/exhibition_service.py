from datetime import datetime

from app.services.base_service import BaseService
from app.repositories.exhibition_repository import ExhibitionRepository


class ExhibitionService(BaseService):
    def __init__(self):
        super().__init__(ExhibitionRepository())

    def to_dict(self, exhibition):
        return {
            'exhibition_id': exhibition.id,
            'title': exhibition.title,
            'description': exhibition.description,
            'start_date': exhibition.start_date,
            'end_date': exhibition.end_date
        }

    def create(self, data):
        exhibition_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'start_date': data.get('start_date'),
            'end_date': data['end_date']
        }
        if exhibition_data['title'] is None:
            return self.error_response("Title cannot be null", 400)
        if exhibition_data['start_date'] and datetime.fromisoformat(exhibition_data['start_date']) < datetime.now():
            return self.error_response("The start date cannot be before the current date", 400)
        if exhibition_data['end_date'] and datetime.fromisoformat(exhibition_data['end_date']) <= datetime.now():
            return self.error_response("The end date cannot be current or before the current date", 400)
        instance = self.repository.create(**exhibition_data)
        return self.to_dict(instance)

    def update(self, exhibition_id, data):
        exhibition = self.repository.get_by_id(exhibition_id)
        exhibition_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'start_date': data.get('start_date'),
            'end_date': data['end_date']
        }
        if exhibition_data['title'] is None:
            return self.error_response("Title cannot be null", 400)
        if exhibition_data['start_date'] and datetime.fromisoformat(exhibition_data['start_date']) < datetime.now():
            return self.error_response("The start date cannot be before the current date", 400)
        if exhibition_data['end_date'] and datetime.fromisoformat(exhibition_data['end_date']) <= datetime.now():
            return self.error_response("The end date cannot be current or before the current date", 400)
        autor = self.repository.update(exhibition, **exhibition_data)
        return self.to_dict(autor)

    def fetch_by_id(self, exhibition_id):
        try:
            exhibition = self.repository.get_by_id(exhibition_id)
            return self.to_dict(exhibition)
        except Exception as e:
            return self.error_response("Exhibition fot found", 404)

    def delete(self, exhibition_id):
        try:
            exhibition = self.repository.get_by_id(exhibition_id)
            self.repository.delete(exhibition)
        except Exception as e:
            return self.error_response("Exhibition fot found", 404)

    def fetch_by_title(self, title):
        result = self.repository.get_by_title(title=title)
        if result is not None:
            return self.to_dict(result)
        return self.error_response("Exhibition fot found", 404)

    def fetch_by_args(self, title=None, start_date=None, end_date=None, work_of_art_name=None):
        results = self.repository.get_by_args(title, start_date, end_date, work_of_art_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]


def exhibition_to_dict(exhibition):
    return {
        'title': exhibition.title,
        'description': exhibition.description,
        'start_date': exhibition.start_date,
        'end_date': exhibition.end_date
    }
