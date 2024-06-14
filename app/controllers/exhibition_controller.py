from flask import jsonify, request

from app.services.exhibition_service import ExhibitionService
from app.controllers.base_controller import base_controller

exhibition_service = ExhibitionService()
exhibition_controller = base_controller(exhibition_service)


def get_by_title(title):
    result = exhibition_service.fetch_by_title(title=title)
    if isinstance(result, dict):
        return jsonify(result)
    return result


def get_by_args():
    title = request.args.get('title')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    items = exhibition_service.fetch_by_args(title, start_date, end_date)
    return jsonify(items)