from app.routes.base_route import base_routes
from app.controllers.visitor_controller import (
    visitor_controller, get_by_name, get_by_args
)

visitor_bp = base_routes(entity_name='visitor',
                           get_all=visitor_controller['get_all'],
                           get_by_id=visitor_controller['get_by_id'],
                           create=visitor_controller['create'],
                           update=visitor_controller['update'],
                           delete=visitor_controller['delete'])
visitor_bp.route('/<string:name>', methods=['GET'])(get_by_name)
visitor_bp.route('', methods=['GET'])(get_by_args)
