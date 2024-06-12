from flask import jsonify, request

from app.services.exhibition_work_of_art_service import ExhibitionWorkOfArtService
from app.controllers.base_controller import base_controller

exhibition_work_of_art_service = ExhibitionWorkOfArtService()
exhibition_work_of_art_controller = base_controller(exhibition_work_of_art_service)


def get_by_args():
    work_of_art_name = request.args.get('work_of_art_name')
    exhibition_name = request.args.get('exhibition_name')

    items = exhibition_work_of_art_service.fetch_by_args(work_of_art_name, exhibition_name)
    return jsonify(items)


def update_by_ids(work_of_art_id, exhibition_id):
    data = request.get_json()
    item = exhibition_work_of_art_service.update(work_of_art_id, exhibition_id, data)
    if isinstance(item, dict):
        return jsonify(item)
    return item


def delete_by_ids(work_of_art_id, exhibition_id):
    result = exhibition_work_of_art_service.delete(work_of_art_id, exhibition_id)
    if result is None:
        return '', 204
    return result


def get_by_work_of_art_id(work_of_art_id):
    result = exhibition_work_of_art_service.fetch_by_work_of_art_id(work_of_art_id)
    if isinstance(result, dict):
        return jsonify(result)
    return result


def get_by_exhibition_id(exhibition_id):
    result = exhibition_work_of_art_service.fetch_by_exhibition_id(exhibition_id)
    if isinstance(result, dict):
        return jsonify(result)
    return result
