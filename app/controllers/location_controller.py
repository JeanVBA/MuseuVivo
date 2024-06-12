from flask import jsonify

from app.services.location_service import LocationService
from app.controllers.base_controller import base_controller

location_service = LocationService()
location_controller = base_controller(location_service)


def get_by_name(name):
    result = location_service.fetch_by_name(name)
    if isinstance(result, dict):
        return jsonify(result)
    return result

