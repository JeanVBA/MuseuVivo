from app.routes.base_route import base_routes
from app.controllers.loan_controller import (loan_controller, get_by_institution_name,
                                             get_by_work_of_art_name, get_by_args)

loan_bp = base_routes(entity_name='loan',
                            get_all=loan_controller['get_all'],
                            get_by_id=loan_controller['get_by_id'],
                            create=loan_controller['create'],
                            update=loan_controller['update'],
                            delete=loan_controller['delete'])
loan_bp.route('/institution/<string:institution_name>', methods=['GET'])(get_by_institution_name)
loan_bp.route('', methods=['GET'])(get_by_args)
loan_bp.route('/work_of_art/<string:work_of_art_name>', methods=['GET'])(get_by_work_of_art_name)
