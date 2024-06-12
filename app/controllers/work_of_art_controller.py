from flask import jsonify, request

from app.services.work_of_art_service import WorkOfArtService
from app.controllers.base_controller import base_controller

work_of_art_service = WorkOfArtService()
work_of_art_controller = base_controller(work_of_art_service)


def get_by_args():
    name = request.args.get('name')
    creation_date = request.args.get('creation_date')
    author_name = request.args.get('author_name')
    location_name = request.args.get('location_name')
    work_of_art_type = request.args.get('type')
    exhibition_name = request.args.get('exhibition_name')

    items = work_of_art_service.fetch_by_args(name, creation_date, author_name, location_name,
                                              work_of_art_type, exhibition_name)
    return jsonify(items)
