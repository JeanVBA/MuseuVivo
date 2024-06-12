from flask import jsonify, request

from app.services.security_service import SecurityService
from app.controllers.base_controller import base_controller

security_service = SecurityService()
security_controller = base_controller(security_service)


def get_by_args():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    location_name = request.args.get('location_name')

    items = security_service.fetch_by_args(name, email, phone, location_name)
    return jsonify(items)


def get_by_name(name):
    result = security_service.fetch_by_name(name)
    if isinstance(result, dict):
        return jsonify(result)
    return result
