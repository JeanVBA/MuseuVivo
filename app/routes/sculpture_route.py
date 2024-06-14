from app.routes.base_route import base_routes
from app.controllers.sculpture_controller import (sculpture_controller, get_by_work_by_name, get_by_args)

sculpture_bp = base_routes(entity_name='sculpture',
                           get_all=sculpture_controller['get_all'],
                           get_by_id=sculpture_controller['get_by_id'],
                           create=sculpture_controller['create'],
                           update=sculpture_controller['update'],
                           delete=sculpture_controller['delete'])
sculpture_bp.route('/work_of_art/<string:work_by_name>', methods=['GET'])(get_by_work_by_name)
sculpture_bp.route('', methods=['GET'])(get_by_args)
