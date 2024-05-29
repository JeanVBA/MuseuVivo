from app.routes.base_route import base_routes
from app.controllers.autor_controller import autor_controller

autor_bp = base_routes(entity_name='autor',
                       get_all=autor_controller['get_all'],
                       get_by_id=autor_controller['get_by_id'],
                       create=autor_controller['create'],
                       update=autor_controller['update'],
                       delete=autor_controller['delete'])
