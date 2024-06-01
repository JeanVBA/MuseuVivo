from app.routes.base_route import base_routes
from app.controllers.escultura_controller import (escultura_controller, get_by_obra_nome)

escultura_bp = base_routes(entity_name='escultura',
                       get_all=escultura_controller['get_all'],
                       get_by_id=escultura_controller['get_by_id'],
                       create=escultura_controller['create'],
                       update=escultura_controller['update'],
                       delete=escultura_controller['delete'])
escultura_bp.route('/obra/<string:obra_nome>', methods=['GET'])(get_by_obra_nome)