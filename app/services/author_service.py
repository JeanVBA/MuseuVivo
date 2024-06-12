from app.services.base_service import BaseService
from app.repositories.author_repository import AuthorRepository


class AuthorService(BaseService):
    def __init__(self):
        super().__init__(AuthorRepository())

    def to_dict(self, author):
        return {
            'id': author.id,
            'name': author.name,
        }

    def create(self, data):
        name = data.get('name')
        if not name:
            return self.error_response("The name field cannot be null", 400)
        instance = self.repository.create(name=name)
        return self.to_dict(instance)

    def update(self, author_id, data):
        author = self.repository.get_by_id(author_id)
        name = data.get('name')
        if author is None:
            return self.error_response("Author not found", 404)
        if not name:
            return self.error_response("The name field cannot be null", 400)
        author = self.repository.update(author, name=name)
        return self.to_dict(author)

    def fetch_by_id(self, author_id):
        try:
            author = self.repository.get_by_id(author_id)
            return self.to_dict(author)
        except Exception as e:
            return self.error_response("Author not found", 404)

    def delete(self, author_id):
        try:
            author = self.repository.get_by_id(author_id)
            self.repository.delete(author)
        except Exception as e:
            return self.error_response("Author not found", 404)

    def fetch_by_name(self, name):
        author = self.repository.get_by_name(name)
        if author is not None:
            return self.to_dict(author)
        return self.error_response("Author not found", 404)

    def fetch_by_args(self, author_id=None, author_name=None):
        results = self.repository.get_by_args(author_id, author_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
