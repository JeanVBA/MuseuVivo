from app.services.ingresso_service import IngressoService
from app.controllers.base_controller import base_controller

ingresso_service = IngressoService()
ingresso_controller = base_controller(ingresso_service)

