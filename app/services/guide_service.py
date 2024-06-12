import re

from app.services.base_service import BaseService
from app.repositories.guide_repository import GuideRepository


class GuideService(BaseService):
    def __init__(self):
        super().__init__(GuideRepository())

    def to_dict(self, guide):
        return {
            'id': guide.id,
            'name': guide.name,
            'email': guide.email,
            'phone': guide.phone
        }

    def create(self, data):
        guide_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        if guide_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if guide_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if guide_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if guide_data['email'] and not re.match(self.email_regex, guide_data['email']):
            return self.error_response("Invalid email format", 400)
        if guide_data['phone'] and not re.match(self.telefone_regex, guide_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.create(**guide_data)
        return self.to_dict(instance)

    def update(self, guide_id, data):
        guide = self.repository.get_by_id(guide_id)
        guide_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        if guide_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if guide_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if guide_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if guide_data['email'] and not re.match(self.email_regex, guide_data['email']):
            return self.error_response("Invalid email format", 400)
        if guide_data['phone'] and not re.match(self.telefone_regex, guide_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.update(guide, **guide_data)
        return self.to_dict(instance)

    def fetch_by_id(self, guide_id):
        try:
            data = self.repository.get_by_id(guide_id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Guide not found", 404)

    def delete(self, guide_id):
        try:
            data = self.repository.get_by_id(guide_id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Guide not found", 404)

    def fetch_by_name(self, name):
        result = self.repository.get_by_name(name)
        if result is not None:
            return self.to_dict(result)
        return self.error_response("Guide not found", 404)

    def fetch_by_args(self, name=None, email=None, phone=None):
        results = self.repository.get_by_args(name, email, phone)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
