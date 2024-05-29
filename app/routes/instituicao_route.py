from app.routes.base_route import base_routes
from app.controllers.instituicao_controller import instituicao_controller


instituicao_bp = base_routes(entity_name='instituicao',
                             get_all=instituicao_controller['get_all'],
                             get_by_id=instituicao_controller['get_by_id'],
                             create=instituicao_controller['create'],
                             update=instituicao_controller['update'],
                             delete=instituicao_controller['delete'])