from flask import request, jsonify

from app.services.painting_service import PaintingService
from app.controllers.base_controller import base_controller

painting_service = PaintingService()
painting_controller = base_controller(painting_service)


def get_by_args():
    work_of_art_name = request.args.get('work_of_art_name')
    technique = request.args.get('technique')

    items = painting_service.fetch_by_args(work_of_art_name, technique)
    return jsonify(items)
