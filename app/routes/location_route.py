from app.routes.base_route import base_routes
from app.controllers.location_controller import (location_controller, get_by_name, get_by_args)

location_bp = base_routes(entity_name='location',
                          get_all=location_controller['get_all'],
                          get_by_id=location_controller['get_by_id'],
                          create=location_controller['create'],
                          update=location_controller['update'],
                          delete=location_controller['delete'])
location_bp.route('/<string:name>', methods=['GET'])(get_by_name)
location_bp.route('', methods=['GET'])(get_by_args)
