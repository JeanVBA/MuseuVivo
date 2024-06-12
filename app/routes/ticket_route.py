from app.routes.base_route import base_routes
from app.controllers.ticket_controller import (ticket_controller, get_by_args)

ticket_bp = base_routes(entity_name='ticket',
                        get_all=ticket_controller['get_all'],
                        get_by_id=ticket_controller['get_by_id'],
                        create=ticket_controller['create'],
                        update=ticket_controller['update'],
                        delete=ticket_controller['delete'])
ticket_bp.route('', methods=['GET'])(get_by_args)
