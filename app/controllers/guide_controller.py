from flask import jsonify, request

from app.services.guide_service import GuideService
from app.controllers.base_controller import base_controller

guide_service = GuideService()
guide_controller = base_controller(guide_service)


def get_by_name(name):
    result = guide_service.fetch_by_name(name)
    if isinstance(result, dict):
        return jsonify(result)
    return result


def get_by_args():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')

    items = guide_service.fetch_by_args(name, email, phone)
    return jsonify(items)
