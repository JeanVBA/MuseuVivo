from decimal import Decimal

from sqlalchemy import event

from app.models.institution_model import Institution
from app.models.ticket_model import Ticket
from app.models.work_of_art_model import WorkOfArt
from app.services.base_service import BaseService
from app.repositories.loan_repository import LoanRepository
from datetime import datetime


class LoanService(BaseService):
    def __init__(self):
        super().__init__(LoanRepository())

    def to_dict(self, loan):
        return {
            'id': loan.id,
            'work_of_art': {
                'id': loan.work_of_art.id,
                'name': loan.work_of_art.name,
                'description': loan.work_of_art.description,
                'creation_date': loan.work_of_art.creation_date,
                'author': loan.work_of_art.author.name if loan.work_of_art.author else None,
                'location': loan.work_of_art.location.name if loan.work_of_art.location else None,
                'type': loan.work_of_art.type
            },
            'loan_date': loan.loan_date,
            'return_date': loan.return_date,
            'institution': loan.institution.name if loan.institution else None,
            'amount_collected': loan.amount_collected
        }
    def create(self, data):
        loan_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'loan_date': data.get('loan_date'),
            'return_date': data.get('return_date'),
            'institution_id': data.get('institution_id'),
            'amount_collected': 0.00
        }
        if loan_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having associated a work of art", 400)
        work_of_art = WorkOfArt.query.get(loan_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if loan_data['return_date'] and datetime.fromisoformat(loan_data['return_date']) < datetime.now():
            return self.error_response("The return date cannot be before the current date", 400)
        if loan_data['institution_id'] is None:
            return self.error_response("Cannot be registered without having associated a institution", 400)
        institution = Institution.query.get(loan_data['institution_id'])
        if institution is None:
            return self.error_response("Institution not found", 404)
        instance = self.repository.create(**loan_data)
        return self.to_dict(instance)

    def update(self, loan_id, data):
        loan = self.repository.get_by_id(loan_id)
        if loan is None:
            return self.error_response("Loan not found", 404)
        loan_data = {
            'work_of_art_id': data.get('work_of_art_id'),
            'loan_date': data.get('loan_date'),
            'return_date': data.get('return_date'),
            'institution_id': data.get('institution_id')
        }
        if loan_data['work_of_art_id'] is None:
            return self.error_response("Cannot be registered without having associated a work of art", 400)
        work_of_art = WorkOfArt.query.get(loan_data['work_of_art_id'])
        if work_of_art is None:
            return self.error_response("Work of art not found", 404)
        if loan_data['return_date'] and datetime.fromisoformat(loan_data['return_date']) < datetime.now():
            return self.error_response("The return date cannot be before the current date", 400)
        if loan_data['institution_id'] is None:
            return self.error_response("Cannot be registered without having associated a institution", 400)
        institution = Institution.query.get(loan_data['institution_id'])
        if institution is None:
            return self.error_response("Institution not found", 404)
        loan = self.repository.update(loan, **loan_data)
        return self.to_dict(loan)

    def fetch_by_id(self, loan_id):
        try:
            loan = self.repository.get_by_id(loan_id)
            return self.to_dict(loan)
        except Exception as e:
            return self.error_response("Loan not found", 404)

    def delete(self, id):
        try:
            loan = self.repository.query.get(id)
            self.repository.delete(loan)
        except Exception as e:
            return self.error_response("Loan not found", 404)

    def fetch_by_institution_name(self, institution_name):
        return [self.to_dict(instance) for instance in self.repository.get_by_institution_name(institution_name)]

    def fetch_by_work_of_art_name(self, work_of_art_name):
        return [self.to_dict(instance) for instance in self.repository.get_by_work_of_art_name(work_of_art_name)]

    def fetch_by_args(self, return_date=None, loan_date=None, work_of_art_name=None, institution_name=None):
        results = self.repository.get_by_args(return_date, loan_date, work_of_art_name, institution_name)
        if results is None:
            return self.error_response("Not found and/or conflicting information", 404)
        return [self.to_dict(result) for result in results]

    def distribute_additional_amount(self, purchase_date, additional_amount):
        loans = self.repository.get_loans_within_dates(purchase_date)
        for loan in loans:
            loan.amount_collected += Decimal(additional_amount)
            self.repository.update_loan(loan)
