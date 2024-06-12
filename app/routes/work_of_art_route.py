from app.routes.base_route import base_routes
from app.controllers.work_of_art_controller import work_of_art_controller, get_by_args

work_of_art_bp = base_routes(entity_name='work_of_art',
                             get_all=work_of_art_controller['get_all'],
                             get_by_id=work_of_art_controller['get_by_id'],
                             create=work_of_art_controller['create'],
                             update=work_of_art_controller['update'],
                             delete=work_of_art_controller['delete'])
work_of_art_bp.route('', methods=['GET'])(get_by_args)
