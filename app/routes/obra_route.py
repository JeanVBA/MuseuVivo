from app.routes.base_route import base_routes
from app.controllers.obra_controller import obra_controller

obra_bp = base_routes(entity_name='obra',
                      get_all=obra_controller['get_all'],
                      get_by_id=obra_controller['get_by_id'],
                      create=obra_controller['create'],
                      update=obra_controller['update'],
                      delete=obra_controller['delete'])