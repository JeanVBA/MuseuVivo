from datetime import datetime, time

from app.models.guide_model import Guide
from app.services.base_service import BaseService
from app.repositories.guided_visits_repository import GuidedVisitRepository

class GuidedVisitService(BaseService):
    def __init__(self):
        super().__init__(GuidedVisitRepository())

    def to_dict(self, guided_visit):
        return {
            'id': guided_visit.id,
            'group': guided_visit.group,
            'visit_date': guided_visit.visit_date,
            'hours': guided_visit.hours.strftime('%H:%M:%S'),
            'guide': {
                'name': guided_visit.guide.name if guided_visit.guide is not None else None,
            }
        }

    def create(self, data):
        guided_visit_data = {
            'group': data.get('group'),
            'visit_date': data.get('visit_date'),
            'hours': data.get('hours'),
            'responsible_guide_id': data['responsible_guide_id']
        }
        if guided_visit_data['responsible_guide_id'] is None:
            return self.error_response("Cannot be registered without having a Guide associated", 400)
        guide = Guide.query.get(guided_visit_data['responsible_guide_id'])
        if guide is None:
            return self.error_response("Guide not found", 404)
        if (guided_visit_data['visit_date'] is None
                or datetime.fromisoformat(guided_visit_data['visit_date']) < datetime.now()):
            return self.error_response("The visit date cannot be before the current date", 400)
        if guided_visit_data['hours'] is None:
            return self.error_response("The hours must be between 9am and 5pm", 400)
        if guided_visit_data['hours']:
            visit_hour = datetime.strptime(guided_visit_data['hours'], '%H:%M').time()
            start_hour = time(9, 0)
            end_hour = time(17, 0)
            if not (start_hour <= visit_hour <= end_hour):
                return self.error_response("The hours must be between 9am and 5pm", 400)
        instance = self.repository.create(**guided_visit_data)
        return self.to_dict(instance)

    def update(self, guided_visit_id, data):
        guided_visit = self.repository.get_by_id(guided_visit_id)
        guided_visit_data = {
            'group': data.get('group'),
            'visit_date': data.get('visit_date'),
            'hours': data.get('hours'),
            'responsible_guide_id': data['responsible_guide_id']
        }
        if guided_visit_data['responsible_guide_id'] is None:
            return self.error_response("Cannot be registered without having a Guide associated", 400)
        guide = Guide.query.get(guided_visit_data['responsible_guide_id'])
        if guide is None:
            return self.error_response("Guide not found", 404)
        if (guided_visit_data['visit_date'] is None
                or datetime.fromisoformat(guided_visit_data['visit_date']) < datetime.now()):
            return self.error_response("The visit date cannot be before the current date", 400)
        if guided_visit_data['hours'] is None:
            return self.error_response("The hours must be between 9am and 5pm", 400)
        if guided_visit_data['hours']:
            visit_hour = datetime.strptime(guided_visit_data['hours'], '%H:%M').time()
            start_hour = time(9, 0)
            end_hour = time(17, 0)
            if not (start_hour <= visit_hour <= end_hour):
                return self.error_response("The hours must be between 9am and 5pm", 400)
        instance = self.repository.update(guided_visit, **guided_visit_data)
        return self.to_dict(instance)

    def fetch_by_id(self, guided_visit_id):
        try:
            instance = self.repository.get_by_id(guided_visit_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Guided Visit not found", 404)

    def delete(self, guided_visit_id):
        try:
            instance = self.repository.get_by_id(guided_visit_id)
            self.repository.delete(instance)
        except Exception as e:
            return self.error_response("Guided Visit not found", 404)

    def fetch_by_args(self, group=None, visit_date=None, hours=None, responsible_guide_name=None):
        results = self.repository.get_by_args(group, visit_date, hours, responsible_guide_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
