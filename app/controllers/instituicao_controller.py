from app.services.instituicao_service import InstituicaoService
from app.controllers.base_controller import base_controller

instituicao_service = InstituicaoService()
instituicao_controller = base_controller(instituicao_service)

