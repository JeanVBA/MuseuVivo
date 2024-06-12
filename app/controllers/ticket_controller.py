from flask import jsonify, request

from app.services.ticket_service import TicketService
from app.controllers.base_controller import base_controller

ticket_service = TicketService()
ticket_controller = base_controller(ticket_service)


def get_by_args():
    ticket_type = request.args.get('type')
    visitor_name = request.args.get('visitor_name')

    items = ticket_service.fetch_by_args(ticket_type, visitor_name)
    return jsonify(items)

