from app.services.exposicao_service import ExposicaoService
from app.controllers.base_controller import base_controller

exposicao_service = ExposicaoService()
exposicao_controller = base_controller(exposicao_service)
