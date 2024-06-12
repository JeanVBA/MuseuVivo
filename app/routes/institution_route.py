from app.routes.base_route import base_routes
from app.controllers.institution_controller import (institution_controller, get_by_args)


institution_bp = base_routes(entity_name='institution',
                             get_all=institution_controller['get_all'],
                             get_by_id=institution_controller['get_by_id'],
                             create=institution_controller['create'],
                             update=institution_controller['update'],
                             delete=institution_controller['delete'])
institution_bp.route('', methods=['GET'])(get_by_args)