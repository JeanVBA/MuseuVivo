from app.routes.base_route import base_routes
from app.controllers.author_controller import (author_controller, get_by_name, get_by_args)

author_bp = base_routes(entity_name='author',
                        get_all=author_controller['get_all'],
                        get_by_id=author_controller['get_by_id'],
                        create=author_controller['create'],
                        update=author_controller['update'],
                        delete=author_controller['delete'])
author_bp.route('/<string:name>', methods=['GET'])(get_by_name)
author_bp.route('', methods=['GET'])(get_by_args)
