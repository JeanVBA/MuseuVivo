from app.services.pintura_service import PinturaService
from app.controllers.base_controller import base_controller

pintura_service = PinturaService()
pintura_controller = base_controller(pintura_service)

