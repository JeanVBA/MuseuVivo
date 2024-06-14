from app.models.loan_model import Loan
from app.repositories.base_repository import BaseRepository
from app.models.institution_model import Institution


class InstitutionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Institution)

    def get_by_args(self, name=None, loan_date=None, return_loan_date=None):
        query = Institution.query
        if name:
            query = query.filter(Institution.name.ilike(f'%{name}%'))
        if return_loan_date:
            query = query.join(Loan).filter(Loan.return_date == return_loan_date)
        if loan_date:
            query = query.join(Loan).filter(Loan.loan_date == loan_date)

        return query.all()
    def get_by_name(self, name):
        return Institution.query.filter_by(name=name).first()
