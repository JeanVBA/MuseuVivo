from app.models.guide_model import Guide
from app.models.ticket_model import Ticket
from app.models.guided_visits_model import GuidedVisit
from app.models.visitor_model import Visitor
from app.services.base_service import BaseService
from app.repositories.ticket_repository import TicketRepository
from datetime import datetime

from app.services.loan_service import LoanService


class TicketService(BaseService):
    def __init__(self):
        super().__init__(TicketRepository())
        self.loan_service = LoanService()

    def to_dict(self, ticket):
        return {
            'id': ticket.id,
            'type': ticket.type,
            'visit_date': ticket.visit_date,
            'purchase_date': ticket.purchase_date,
            'visitor': {
                'name': ticket.visitor.name if ticket.visitor else None,
            },
            'guided_visit': {
                'group': ticket.guided_visit.group if ticket.guided_visit else "Guided tour canceled",
                'guide': {
                    'name': ticket.guided_visit.guide.name if ticket.guided_visit else "No guide"
                }
            }
        }

    def create(self, data):
        ticket_data = {
            'visitor_id': data.get('visitor_id'),
            'type': data.get('type'),
            'visit_date': data.get('visit_date'),
            'purchase_date': data.get('purchase_date'),
            'guided_visit_id': data.get('guided_visit_id')
        }

        if ticket_data['visitor_id'] is None:
            return self.error_response("Cannot be registered without having a visitor associated", 400)
        visitor = Visitor.query.get(ticket_data['visitor_id'])
        if visitor is None:
            return self.error_response("Visitor not found", 404)
        if ticket_data['type'] not in ['Silver', 'Gold', 'Premium']:
            return self.error_response("Ticket type must be 'Silver, Gold or Premium'", 400)
        if ticket_data['type'] == 'Silver':
            ticket_data['price'] = 50.00
        elif ticket_data['type'] == 'Gold':
            ticket_data['price'] = 100.00
        elif ticket_data['type'] == 'Premium':
            ticket_data['price'] = 150.00
        if ticket_data['visit_date'] and datetime.fromisoformat(ticket_data['visit_date']) < datetime.now():
            return self.error_response("The visit date cannot be before the current date", 400)
        if ticket_data['guided_visit_id'] is None:
            return self.error_response("Cannot be registered without having a Guided Visit associated", 400)
        guided_visit = GuidedVisit.query.get(ticket_data['guided_visit_id'])
        if guided_visit is None:
            return self.error_response("Guided Visit not found", 404)
        instance = self.repository.create(**ticket_data)
        additional_amount = ticket_data['price'] * 0.01
        self.loan_service.distribute_additional_amount(ticket_data['purchase_date'], additional_amount)
        return self.to_dict(instance)

    def update(self, ticket_id, data):
        ticket = self.repository.get_by_id(ticket_id)
        ticket_data = {
            'visitor_id': data.get('visitor_id'),
            'type': data.get('type'),
            'visit_date': data.get('visit_date'),
            'purchase_date': data.get('purchase_date'),
            'guided_visit_id': data.get('guided_visit_id')
        }

        if ticket_data['visitor_id'] is None:
            return self.error_response("Cannot be registered without having a visitor associated", 400)
        visitor = Visitor.query.get(ticket_data['visitor_id'])
        if visitor is None:
            return self.error_response("Visitor not found", 404)
        if ticket_data['type'] not in ['Silver', 'Gold', 'Premium']:
            return self.error_response("Ticket type must be 'Silver, Gold or Premium'", 400)
        if ticket_data['type'] == 'Silver':
            ticket_data['price'] = 50.00
        elif ticket_data['type'] == 'Gold':
            ticket_data['price'] = 100.00
        elif ticket_data['type'] == 'Premium':
            ticket_data['price'] = 150.00
        if ticket_data['visit_date'] and datetime.fromisoformat(ticket_data['visit_date']) < datetime.now():
            return self.error_response("The visit date cannot be before the current date", 400)
        if ticket_data['guided_visit_id'] is None:
            return self.error_response("Cannot be registered without having a Guided Visit associated", 400)
        guided_visit = GuidedVisit.query.get(ticket_data['guided_visit_id'])
        if guided_visit is None:
            return self.error_response("Guided Visit not found", 404)
        instance = self.repository.update(ticket, **ticket_data)
        return self.to_dict(instance)

    def fetch_by_id(self, ticket_id):
        try:
            instance = self.repository.get_by_id(ticket_id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Ticket not found", 404)

    def delete(self, ticket_id):
        try:
            ticket = self.repository.get_by_id(ticket_id)
            self.repository.delete(ticket)
        except Exception as e:
            return self.error_response("Ticket not found", 404)

    def fetch_by_args(self, ticket_type=None, visitor_name=None):
        results = self.repository.get_by_args(ticket_type, visitor_name)
        return [self.to_dict(result) for result in results]


def ticket_to_dict(ticket):
    return {
            'id': ticket.id,
            'type': ticket.type,
            'visit_date': ticket.visit_date,
            'purchase_date': ticket.purchase_date,
            'guided_visit': {
                'group': ticket.guided_visit.group if ticket.guided_visit else None,
                'guide': {
                    'name': ticket.guided_visit.guide.name if ticket.guided_visit.guide else None
                }
            }
        }