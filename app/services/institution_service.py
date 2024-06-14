from app.models.institution_model import Institution
from app.services.base_service import BaseService
from app.repositories.institution_repository import InstitutionRepository
from app.services.work_of_art_service import work_of_art_to_dict

class InstitutionService(BaseService):
    def __init__(self):
        super().__init__(InstitutionRepository())

    def to_dict(self, institution):
        return {
            'id': institution.id,
            'name': institution.name,
            'works_of_art': [work_of_art_to_dict(loan.work_of_art) for loan in institution.loans]
        }

    def create(self, data):
        name = data.get('name')
        if name is None:
            return self.error_response('Name field must be filled in', 400)
        instance = self.repository.create(name=name)
        return self.to_dict(instance)

    def update(self, institution_id, data):
        institution = self.repository.get_by_id(institution_id)
        name = data.get('name')
        if name is None:
            return self.error_response('Name field must be filled in', 400)
        instance = self.repository.update(institution, name=name)
        return self.to_dict(instance)

    def fetch_by_id(self, institution_id):
        try:
            institution = self.repository.get_by_id(institution_id)
            return self.to_dict(institution)
        except Exception as e:
            return self.error_response("Institution not found", 404)

    def delete(self, institution_id):
        try:
            institution = self.repository.get_by_id(institution_id)
            self.repository.delete(institution)
        except Exception as e:
            return self.error_response("Institution not found", 404)

    def fetch_by_args(self, name=None, loan_date=None, return_loan_date=None):
        results = self.repository.get_by_args(name, loan_date, return_loan_date)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]
