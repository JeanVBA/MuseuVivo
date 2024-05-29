from app.services.escultura_service import EsculturaService
from app.controllers.base_controller import base_controller

escultura_service = EsculturaService()
escultura_controller = base_controller(escultura_service)
