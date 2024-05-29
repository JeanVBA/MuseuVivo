from app.controllers.base_controller import base_controller
from app.services.visitaGuiada_service import VisitaGuiadaService

visitaGuiada_service = VisitaGuiadaService()
visitaGuiada_controller = base_controller(visitaGuiada_service)
