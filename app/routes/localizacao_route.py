from app.routes.base_route import base_routes
from app.controllers.localizacao_controller import localizacao_controller


localizacao_bp = base_routes(entity_name='localizacao',
                             get_all=localizacao_controller['get_all'],
                             get_by_id=localizacao_controller['get_by_id'],
                             create=localizacao_controller['create'],
                             update=localizacao_controller['update'],
                             delete=localizacao_controller['delete'])
