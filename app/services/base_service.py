from flask import jsonify

class BaseService:
    def __init__(self, repository):
        self.repository = repository

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    telefone_regex = r'^\+?[1-9]\d{1,14}$'

    def to_dict(self, instance):
        raise NotImplementedError("The 'to_dict' method must be implemented.")

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        instances = self.repository.get_all()
        return [self.to_dict(instance) for instance in instances]

    def fetch_by_id(self, object_id):
        instance = self.repository.get_by_id(object_id)
        return self.to_dict(instance)

    def create(self, data):
        instance = self.repository.create(**data)
        return self.to_dict(instance)

    def update(self, object_id, data):
        instance = self.repository.get_by_id(object_id)
        instance = self.repository.update(instance, **data)
        return self.to_dict(instance)

    def delete(self, object_id):
        instance = self.repository.get_by_id(object_id)
        self.repository.delete(instance)