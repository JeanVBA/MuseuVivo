from sqlalchemy import and_
from app import db
from app.models.loan_model import Loan
from app.models.visitor_model import Visitor
from app.repositories.base_repository import BaseRepository
from app.models.ticket_model import Ticket


class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)

    def get_by_loans(self, purchase_date):
        return Loan.query.filter(
            and_(
                Loan.loan_date < purchase_date,
                Loan.return_date > purchase_date
            )
        ).all()
    def get_by_args(self, ticket_type=None, visitor_name=None):
        query = Ticket.query
        if ticket_type:
            query = query.filter(Ticket.type.ilike(f'%{ticket_type}%'))
        if visitor_name:
            query = query.join(Visitor).filter(Visitor.name.ilike(f'%{visitor_name}%'))
        return query.all()

    def get_by_type(self, ticket_type):
        return Ticket.query.filter_by(type=ticket_type).all()
