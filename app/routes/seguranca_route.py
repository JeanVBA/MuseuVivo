from app.routes.base_route import base_routes
from app.controllers.seguranca_controller import (
    seguranca_controller, get_by_name
)

seguranca_bp = base_routes(entity_name='seguranca',
                           get_all=seguranca_controller['get_all'],
                           get_by_id=seguranca_controller['get_by_id'],
                           create=seguranca_controller['create'],
                           update=seguranca_controller['update'],
                           delete=seguranca_controller['delete'])
seguranca_bp.route('/<string:nome>', methods=['GET'])(get_by_name)
