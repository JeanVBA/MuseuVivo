from flask import jsonify, request

from app.services.visitor_service import VisitorService
from app.controllers.base_controller import base_controller

visitor_service = VisitorService()
visitor_controller = base_controller(visitor_service)


def get_by_args():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')

    items = visitor_service.fetch_by_args(name, email, phone)
    return jsonify(items)


def get_by_name(name):
    result = visitor_service.fetch_by_name(name)
    if isinstance(result, dict):
        return jsonify(result)
    return result
