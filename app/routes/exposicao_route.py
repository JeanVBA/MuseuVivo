from app.routes.base_route import base_routes
from app.controllers.exposicao_controller import exposicao_controller

exposicao_bp = base_routes(entity_name='exposicao',
                           get_all=exposicao_controller['get_all'],
                           get_by_id=exposicao_controller['get_by_id'],
                           create=exposicao_controller['create'],
                           update=exposicao_controller['update'],
                           delete=exposicao_controller['delete'])
