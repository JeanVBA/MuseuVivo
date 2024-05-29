from app.services.obra_service import ObraService
from app.controllers.base_controller import base_controller

obra_service = ObraService()
obra_controller = base_controller(obra_service)

