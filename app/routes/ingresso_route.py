from app.routes.base_route import base_routes
from app.controllers.ingresso_controller import (ingresso_controller, get_by_args)

ingresso_bp = base_routes(entity_name='ingresso',
                       get_all=ingresso_controller['get_all'],
                       get_by_id=ingresso_controller['get_by_id'],
                       create=ingresso_controller['create'],
                       update=ingresso_controller['update'],
                       delete=ingresso_controller['delete'])
ingresso_bp.route('', methods=['GET'])(get_by_args)