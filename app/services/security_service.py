import re

from app.models.location_model import Location
from app.services.base_service import BaseService
from app.repositories.security_repository import SecurityRepository


class SecurityService(BaseService):
    def __init__(self):
        super().__init__(SecurityRepository())

    def to_dict(self, security):
        return  {
            'id': security.id,
            'name': security.name,
            'email': security.email,
            'phone': security.phone,
            'location': security.location.name if security.location else None
        }

    def create(self, data):
        security_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'location_id': data.get('location_id'),
        }
        if security_data['location_id'] is None:
            return self.error_response("Cannot be registered without having a Location associated", 400)
        location = Location.query.get(security_data['location_id'])
        if location is None:
            return self.error_response("Location not found", 400)
        if  security_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if security_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if security_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if security_data['email'] and not re.match(self.email_regex, security_data['email']):
            return self.error_response("Invalid email format", 400)
        if security_data['phone'] and not re.match(self.telefone_regex, security_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.create(**security_data)
        return self.to_dict(instance)

    def update(self, security_id, data):
        security = self.repository.get_by_id(security_id)
        security_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'location_id': data.get('location_id'),
        }
        if security_data['location_id'] is None:
            return self.error_response("Cannot be registered without having a Location associated", 400)
        location = Location.query.get(security_data['location_id'])
        if location is None:
            return self.error_response("Location not found", 400)
        if security_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if security_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if security_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if security_data['email'] and not re.match(self.email_regex, security_data['email']):
            return self.error_response("Invalid email format", 400)
        if security_data['phone'] and not re.match(self.telefone_regex, security_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.update(security, **security_data)
        return self.to_dict(instance)

    def fetch_by_id(self, security_id):
        try:
            data = self.repository.get_by_id(security_id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Security not found", 404)

    def delete(self, security_id):
        try:
            data = self.repository.get_by_id(security_id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Security not found", 404)

    def fetch_by_name(self, name):
        result = self.repository.get_by_name(name)
        if result is not None:
            return self.to_dict(result)
        return self.error_response("Security not found", 404)

    def fetch_by_args(self, name=None, email=None, phone=None, location_name=None):
        results = self.repository.get_by_args(name, email, phone, location_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]