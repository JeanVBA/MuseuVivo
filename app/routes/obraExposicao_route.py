from app.routes.base_route import base_routes
from app.controllers.obraExposicao_controller import (
    obraExposicao_controller,
    get_by_obraId,
    get_by_Exposicaoid,
    update_by_ids,
    delete_by_ids,
)

obraExposicao_bp = base_routes(entity_name='obraExposicao',
                               get_all=obraExposicao_controller['get_all'],
                               get_by_id=obraExposicao_controller['get_by_id'],
                               create=obraExposicao_controller['create'],
                               update=obraExposicao_controller['update'],
                               delete=obraExposicao_controller['delete'])
obraExposicao_bp.route('/exposicao/<int:id>', methods=['GET'])(get_by_Exposicaoid)
obraExposicao_bp.route('/obra/<int:id>', methods=['GET'])(get_by_obraId)
obraExposicao_bp.route('/obraId/<int:obra_id>/exposicaoId/<int:exposicao_id>', methods=['PUT'])(update_by_ids)
obraExposicao_bp.route('/obraId/<int:obra_id>/exposicaoId/<int:exposicao_id>', methods=['DELETE'])(delete_by_ids)