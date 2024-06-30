from app import db
from app.models.institution_model import Institution
from app.models.work_of_art_model import WorkOfArt
from app.repositories.base_repository import BaseRepository
from app.models.loan_model import Loan


class LoanRepository(BaseRepository):
    def __init__(self):
        super().__init__(Loan)

    def get_loans_within_dates(self, purchase_date):
        return Loan.query.filter(
            Loan.loan_date <= purchase_date,
            Loan.return_date >= purchase_date
        ).all()

    def update_loan(self, loan):
        db.session.add(loan)
        db.session.commit()

    def get_by_args(self, return_date=None, loan_date=None, work_of_art_name=None, institution_name=None):
        query = Loan.query
        if return_date:
            query = query.filter(Loan.return_date == return_date)
        if loan_date:
            query = query.filter(Loan.loan_date == loan_date)
        if work_of_art_name:
            query = query.join(Loan.work_of_art).filter(WorkOfArt.name.ilike(f'%{work_of_art_name}%'))
        if institution_name:
            query = query.join(Loan.institution).filter(Institution.name.ilike(f'%{institution_name}%'))
        return query.all()

    def get_by_work_of_art_name(self, work_of_art_name):
        return Loan.query.join(Loan.work_of_art).filter(WorkOfArt.name.ilike(f'%{work_of_art_name}%')).all()

    def get_by_institution_name(self, institution_name):
        return Loan.query.join(Loan.institution).filter(Institution.name.ilike(f'%{institution_name}%')).all()