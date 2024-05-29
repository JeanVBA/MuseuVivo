from app.controllers.base_controller import base_controller
from app.services.autor_service import AutorService

autor_service = AutorService()
autor_controller = base_controller(autor_service)

