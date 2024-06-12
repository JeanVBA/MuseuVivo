from flask import jsonify, request

from app.controllers.base_controller import base_controller
from app.services.author_service import AuthorService

author_service = AuthorService()
author_controller = base_controller(author_service)

def get_by_name(name):
    result = author_service.fetch_by_name(name)
    if isinstance(result, dict):
        return jsonify(result)
    return result
def get_by_args():
    author_id = request.args.get('id')
    author_name = request.args.get('name')

    items = author_service.fetch_by_args(author_id, author_name)
    return jsonify(items)