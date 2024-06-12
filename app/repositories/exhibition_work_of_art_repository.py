from app import db
from app.repositories.base_repository import BaseRepository
from app.models.exhibition_work_of_art_model import ExhibitionWorkOfArt


class ExhibitionWorkOfArtRepository(BaseRepository):
    def __init__(self):
        super().__init__(ExhibitionWorkOfArt)

    def get_by_args(self, work_of_art_name=None, exhibition_name=None):
        query = ExhibitionWorkOfArt.query
        if work_of_art_name:
            query = query.filter(ExhibitionWorkOfArt.work_of_art.name.ilike(f'%{work_of_art_name}%'))
        if exhibition_name:
            query = query.filter(ExhibitionWorkOfArt.exhibition.name.ilike(f'%{exhibition_name}%'))
        return query.all()

    def update_by_ids(self, instance):
        db.session.commit()
        return instance

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()

    def get_by_ids(self, work_of_art_id, exhibition_id):
        return ExhibitionWorkOfArt.query.filter_by(work_of_art_id=work_of_art_id, exhibition_id=exhibition_id).first()

    def get_by_work_of_art_id(self, work_of_art_id):
        return self.model.query.filter_by(work_of_art_id=work_of_art_id).all()

    def get_by_exhibition_id(self, exhibition_id):
        return self.model.query.filter_by(exhibition_id=exhibition_id).all()
