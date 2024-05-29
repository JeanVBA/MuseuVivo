from flask import Blueprint


def base_routes(entity_name, get_all, get_by_id, create, update, delete):
    bp = Blueprint(f'{entity_name}_bp', __name__, url_prefix=f'/{entity_name}')

    bp.route('/', methods=['GET'])(get_all)
    bp.route('/<int:id>', methods=['GET'])(get_by_id)
    bp.route('/', methods=['POST'])(create)
    bp.route('/<int:id>', methods=['PUT'])(update)
    bp.route('/<int:id>', methods=['DELETE'])(delete)

    return bp