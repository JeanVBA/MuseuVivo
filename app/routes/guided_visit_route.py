from app.routes.base_route import base_routes
from app.controllers.guided_visit_controller import guided_visit_controller, get_by_args

guided_visit_bp = base_routes(entity_name='guided_visit',
                              get_all=guided_visit_controller['get_all'],
                              get_by_id=guided_visit_controller['get_by_id'],
                              create=guided_visit_controller['create'],
                              update=guided_visit_controller['update'],
                              delete=guided_visit_controller['delete'])
guided_visit_bp.route('', methods=['GET'])(get_by_args)
