import re

from app.services.base_service import BaseService
from app.repositories.visitor_repository import VisitorRepository
from app.services.ticket_service import ticket_to_dict


class VisitorService(BaseService):
    def __init__(self):
        super().__init__(VisitorRepository())

    def to_dict(self, visitor):
        return {
            'id': visitor.id,
            'name': visitor.name,
            'email': visitor.email,
            'phone': visitor.phone,
            'tickets': [ticket_to_dict(tickets)
                        for tickets in visitor.tickets]
        }

    def create(self, data):
        visitor_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        if visitor_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if visitor_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if visitor_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if visitor_data['email'] and not re.match(self.email_regex, visitor_data['email']):
            return self.error_response("Invalid email format", 400)
        if visitor_data['phone'] and not re.match(self.telefone_regex, visitor_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.create(**visitor_data)
        return self.to_dict(instance)

    def update(self, visitor_id, data):
        visitor = self.repository.get_by_id(visitor_id)
        visitor_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
        }
        if visitor_data['name'] is None:
            return self.error_response("Name field must be filled in", 400)
        if visitor_data['email'] is None:
            return self.error_response("Email field must be filled in", 400)
        if visitor_data['phone'] is None:
            return self.error_response("Phone field must be filled in", 400)
        if visitor_data['email'] and not re.match(self.email_regex, visitor_data['email']):
            return self.error_response("Invalid email format", 400)
        if visitor_data['phone'] and not re.match(self.telefone_regex, visitor_data['phone']):
            return self.error_response("Invalid phone format", 400)
        instance = self.repository.update(visitor, **visitor_data)
        return self.to_dict(instance)

    def fetch_by_id(self, visitor_id):
        try:
            data = self.repository.get_by_id(visitor_id)
            return self.to_dict(data)
        except Exception as e:
            return self.error_response("Visitor not found", 404)

    def delete(self, visitor_id):
        try:
            data = self.repository.get_by_id(visitor_id)
            self.repository.delete(data)
        except Exception as e:
            return self.error_response("Visitor not found", 404)

    def fetch_by_name(self, name):
        result = self.repository.get_by_name(name)
        if result is not None:
            return self.to_dict(result)
        return self.error_response("Visitor not found", 404)

    def fetch_by_args(self, name=None, email=None, phone=None):
        results = self.repository.get_by_args(name, email, phone)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
