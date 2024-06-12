from app.routes.base_route import base_routes
from app.controllers.exhibition_work_of_art_controller import (
    exhibition_work_of_art_controller,
    get_by_work_of_art_id,
    get_by_exhibition_id,
    update_by_ids,
    delete_by_ids,
)

exhibition_work_of_art_bp = base_routes(entity_name='exhibition_work_of_art',
                               get_all=exhibition_work_of_art_controller['get_all'],
                               get_by_id=exhibition_work_of_art_controller['get_by_id'],
                               create=exhibition_work_of_art_controller['create'],
                               update=exhibition_work_of_art_controller['update'],
                               delete=exhibition_work_of_art_controller['delete'])
exhibition_work_of_art_bp.route('/exhibition/<int:exhibition_id>', methods=['GET'])(get_by_exhibition_id)
exhibition_work_of_art_bp.route('/work_of_art/<int:work_of_art_id>', methods=['GET'])(get_by_work_of_art_id)
exhibition_work_of_art_bp.route('/work_of_art_id/<int:work_of_art_id>/exhibition_id/<int:exhibition_id>',
                                methods=['PUT'])(update_by_ids)
exhibition_work_of_art_bp.route('/work_of_art_id/<int:work_of_art_id>/exhibition_id/<int:exhibition_id>',
                                methods=['DELETE'])(delete_by_ids)