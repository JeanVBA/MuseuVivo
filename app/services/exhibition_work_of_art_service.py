from app.models.exhibition_model import Exhibition
from app.models.work_of_art_model import WorkOfArt
from app.services.base_service import BaseService
from app.services.work_of_art_service import work_of_art_to_dict
from app.services.exhibition_service import exhibition_to_dict
from app.repositories.exhibition_work_of_art_repository import ExhibitionWorkOfArtRepository


class ExhibitionWorkOfArtService(BaseService):
    def __init__(self):
        super().__init__(ExhibitionWorkOfArtRepository())

    def to_dict(self, instance):
        return {
            'work_of_art_id': instance.work_of_art_id,
            'work_of_art_name': instance.work_of_art.name,
            'exhibition_id': instance.exhibition_id if instance.exhibition_id else None,
            'exhibition_title': instance.exhibition.title if instance.exhibition.title else None,
        }

    def exhibitions_to_dict(self, instance):
        return {
            'exhibition_id': instance.exposicao_id,
            'exhibition_title': instance.exposicao.titulo,
            'works_of_art': [work_of_art_to_dict(exhibition_work_of_art.work_of_art)
                             for exhibition_work_of_art in instance.exhibition.works_of_art_exhibitions]
        }

    def works_of_art_to_dict(self, instance):
        return {
            'work_of_art_id': instance.obra_id,
            'work_of_art_name': instance.obra.nome,
            'exhibitions': [exhibition_to_dict(exhibition_work_of_art.exhibition)
                           for exhibition_work_of_art in instance.work_of_art.works_of_art_exhibitions]
        }

    def create(self, data):
        work_of_art_id = data.get('work_of_art_id')
        exhibition_id = data.get('exhibition_id')

        if work_of_art_id is None or exhibition_id is None:
            return self.error_response("Work of art - Id and Exhibition - Id must be provided", 400)
        work_of_art = WorkOfArt.query.get(work_of_art_id)
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        exhibition = Exhibition.query.get(exhibition_id)
        if exhibition is None:
            return self.error_response("Exhibition not found", 404)

        instance = self.repository.create(work_of_art_id=work_of_art_id, exhibition_id=exhibition_id)
        return self.to_dict(instance)

    def update(self, work_of_art_id, exhibition_id, data):
        exhibition_work_of_art = self.repository.get_by_ids(work_of_art_id, exhibition_id)
        if exhibition_work_of_art is None:
            return self.error_response("Relationship not found", 404)

        work_of_art_id = data.get('work_of_art_id')
        exhibition_id = data.get('exhibition_id')

        if work_of_art_id is not None:
            work_of_art = WorkOfArt.query.get(work_of_art_id)
            if work_of_art is None:
                return self.error_response("Work of art not found", 404)
            exhibition_work_of_art.work_of_art_id = work_of_art_id

        if exhibition_id is not None:
            exhibition = Exhibition.query.get(exhibition_id)
            if exhibition is None:
                return self.error_response("Exhibition not found", 404)
            exhibition_work_of_art.exhibition_id = exhibition_id

        instance = self.repository.update_by_ids(exhibition_work_of_art)
        return self.to_dict(instance)

    def fetch_by_work_of_art_id(self, work_of_art_id):
        exhibitions_work_of_art = self.repository.get_by_work_of_art_id(work_of_art_id)
        works_of_art_set = set()
        unique_results = []
        for result in exhibitions_work_of_art:
            if result.work_of_art_id not in works_of_art_set:
                works_of_art_set.add(result.work_of_art_id)
                unique_results.append(result)
        if not unique_results:
            return {"message": "No records found"}, 404
        if exhibitions_work_of_art is not None:
            return [self.works_of_art_to_dict(result) for result in unique_results]
        return self.error_response("Work of art not found", 404)

    def fetch_by_exhibition_id(self, exhibition_id):
        exhibition_works_of_art = self.repository.get_by_exhibition_id(exhibition_id)
        exhibitions_set = set()
        unique_results = []
        for result in exhibition_works_of_art:
            if result.exhibition_id not in exhibitions_set:
                exhibitions_set.add(result.exhibition_id)
                unique_results.append(result)
        if not unique_results:
            return {"message": "No records found"}, 404
        if exhibition_works_of_art is not None:
            return [self.exhibitions_to_dict(result) for result in unique_results]
        return self.error_response("Exhibition not found", 404)

    def delete(self, work_of_art_id, exhibition_id):
        exhibition_work_of_art = self.repository.get_by_ids(work_of_art_id, exhibition_id)
        if exhibition_work_of_art is None:
            return self.error_response("Relationship not found", 404)
        self.repository.delete(exhibition_work_of_art)
        return None

    def fetch_by_args(self, work_of_art_name=None, exhibition_name=None):
        results = self.repository.get_by_args(work_of_art_name, exhibition_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
