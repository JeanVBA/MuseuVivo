from app.routes.base_route import base_routes
from app.controllers.visitante_controller import (
    visitante_controller, get_by_name
)

visitante_bp = base_routes(entity_name='visitante',
                           get_all=visitante_controller['get_all'],
                           get_by_id=visitante_controller['get_by_id'],
                           create=visitante_controller['create'],
                           update=visitante_controller['update'],
                           delete=visitante_controller['delete'])
visitante_bp.route('/<string:nome>', methods=['GET'])(get_by_name)
