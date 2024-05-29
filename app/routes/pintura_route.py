from app.routes.base_route import base_routes
from app.controllers.pintura_controller import pintura_controller

pintura_bp = base_routes(entity_name='pintura',
                       get_all=pintura_controller['get_all'],
                       get_by_id=pintura_controller['get_by_id'],
                       create=pintura_controller['create'],
                       update=pintura_controller['update'],
                       delete=pintura_controller['delete'])
