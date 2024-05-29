from app.routes.base_route import base_routes
from app.controllers.visitante_controller import (
    get_visitantes,
    get_visitante,
    create_visitante,
    update_visitante,
    delete_visitante
)

visitante_bp = base_routes(entity_name='visitante',
                       get_all=get_visitantes,
                       get_by_id=get_visitante,
                       create=create_visitante,
                       update=update_visitante,
                       delete=delete_visitante)
