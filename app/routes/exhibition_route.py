from app.routes.base_route import base_routes
from app.controllers.exhibition_controller import (exhibition_controller, get_by_title, get_by_args)

exhibition_bp = base_routes(entity_name='exhibition',
                           get_all=exhibition_controller['get_all'],
                           get_by_id=exhibition_controller['get_by_id'],
                           create=exhibition_controller['create'],
                           update=exhibition_controller['update'],
                           delete=exhibition_controller['delete'])
exhibition_bp.route('/<string:title>', methods=['GET'])(get_by_title)
exhibition_bp.route('', methods=['GET'])(get_by_args)
