from app.services.localizacao_service import LocalizacaoService
from app.controllers.base_controller import base_controller

localizacao_service = LocalizacaoService()
localizacao_controller = base_controller(localizacao_service)

