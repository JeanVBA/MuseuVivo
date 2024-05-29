from app.services.guia_service import GuiaService
from app.controllers.base_controller import base_controller

guia_service = GuiaService()
guia_controller = base_controller(guia_service)

