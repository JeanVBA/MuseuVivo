from app.routes.base_route import base_routes
from app.controllers.seguranca_controller import (
    get_segurancas,
    get_seguranca,
    create_seguranca,
    update_seguranca,
    delete_seguranca
)

seguranca_bp = base_routes(entity_name='seguranca',
                       get_all=get_segurancas,
                       get_by_id=get_seguranca,
                       create=create_seguranca,
                       update=update_seguranca,
                       delete=delete_seguranca)
