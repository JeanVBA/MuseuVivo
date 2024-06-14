from app.repositories.base_repository import BaseRepository
from app.models.author_model import Author


class AuthorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Author)

    def get_by_name(self, name):
        return Author.query.filter_by(name=name).first()

    def get_by_args(self, author_id=None, name=None):
        query = Author.query
        if author_id:
            query = query.filter(Author.id == author_id)
        if name:
            query = query.filter(Author.name == name)
        return query.all()
