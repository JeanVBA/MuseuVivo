from app.routes.base_route import base_routes
from app.controllers.guia_controller import guia_controller
guia_bp = base_routes(entity_name='guia',
                      get_all=guia_controller['get_all'],
                      get_by_id=guia_controller['get_by_id'],
                      create=guia_controller['create'],
                      update=guia_controller['update'],
                      delete=guia_controller['delete'])
