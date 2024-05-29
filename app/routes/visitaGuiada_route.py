from app.routes.base_route import base_routes
from app.controllers.visitaGuiada_controller import visitaGuiada_controller

visitaGuiada_bp = base_routes(entity_name='visitaGuiada',
                       get_all=visitaGuiada_controller['get_all'],
                       get_by_id=visitaGuiada_controller['get_by_id'],
                       create=visitaGuiada_controller['create'],
                       update=visitaGuiada_controller['update'],
                       delete=visitaGuiada_controller['delete'])
