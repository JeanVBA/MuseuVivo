from app.routes.base_route import base_routes
from app.controllers.escultura_controller import escultura_controller

escultura_bp = base_routes(entity_name='escultura',
                       get_all=escultura_controller['get_all'],
                       get_by_id=escultura_controller['get_by_id'],
                       create=escultura_controller['create'],
                       update=escultura_controller['update'],
                       delete=escultura_controller['delete'])
