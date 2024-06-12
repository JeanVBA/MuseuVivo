from app.routes.base_route import base_routes
from app.controllers.security_controller import (
    security_controller, get_by_name, get_by_args
)

security_bp = base_routes(entity_name='security',
                          get_all=security_controller['get_all'],
                          get_by_id=security_controller['get_by_id'],
                          create=security_controller['create'],
                          update=security_controller['update'],
                          delete=security_controller['delete'])
security_bp.route('/<string:name>', methods=['GET'])(get_by_name)
security_bp.route('', methods=['GET'])(get_by_args)