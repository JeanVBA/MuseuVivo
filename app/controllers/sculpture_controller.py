from flask import jsonify, request

from app.services.sculpture_service import SculptureService
from app.controllers.base_controller import base_controller

sculpture_service = SculptureService()
sculpture_controller = base_controller(sculpture_service)


def get_by_work_by_name(work_by_name):
    result = sculpture_service.fetch_by_work_of_art_name(work_by_name)
    if isinstance(result, dict):
        return jsonify(result)
    return result


def get_by_args():
    work_of_art_name = request.args.get('work_of_art_name')
    material = request.args.get('material')
    weight = request.args.get('weight')

    items = sculpture_service.fetch_by_args(work_of_art_name, material, weight)
    return jsonify(items)