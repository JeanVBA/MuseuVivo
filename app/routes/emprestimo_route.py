from app.routes.base_route import base_routes
from app.controllers.emprestimo_controller import emprestimo_controller

emprestimo_bp = base_routes(entity_name='emprestimo',
                            get_all=emprestimo_controller['get_all'],
                            get_by_id=emprestimo_controller['get_by_id'],
                            create=emprestimo_controller['create'],
                            update=emprestimo_controller['update'],
                            delete=emprestimo_controller['delete'])