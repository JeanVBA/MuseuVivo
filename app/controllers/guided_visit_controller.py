from flask import request, jsonify

from app.controllers.base_controller import base_controller
from app.services.guided_visit_service import GuidedVisitService

guided_visit_service = GuidedVisitService()
guided_visit_controller = base_controller(guided_visit_service)


def get_by_args():
    group = request.args.get('group')
    visit_date = request.args.get('visit_date')
    hours = request.args.get('hours')
    responsible_guide_name = request.args.get('responsible_guide')

    items = guided_visit_service.fetch_by_args(group, visit_date, hours, responsible_guide_name)
    return jsonify(items)