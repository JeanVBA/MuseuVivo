from app.routes.base_route import base_routes
from app.controllers.guide_controller import (guide_controller, get_by_name, get_by_args)

guide_bp = base_routes(entity_name='guide',
                       get_all=guide_controller['get_all'],
                       get_by_id=guide_controller['get_by_id'],
                       create=guide_controller['create'],
                       update=guide_controller['update'],
                       delete=guide_controller['delete'])
guide_bp.route('/<string:name>', methods=['GET'])(get_by_name)
guide_bp.route('', methods=['GET'])(get_by_args)
