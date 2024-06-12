from app.routes.base_route import base_routes
from app.controllers.painting_controller import painting_controller, get_by_args

painting_bp = base_routes(entity_name='painting',
                          get_all=painting_controller['get_all'],
                          get_by_id=painting_controller['get_by_id'],
                          create=painting_controller['create'],
                          update=painting_controller['update'],
                          delete=painting_controller['delete'])
painting_bp.route('', methods=['GET'])(get_by_args)
