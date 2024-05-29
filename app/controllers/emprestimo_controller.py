from app.controllers.base_controller import base_controller
from app.services.emprestimo_service import EmprestimoService

emprestimo_service = EmprestimoService()
emprestimo_controller = base_controller(emprestimo_service)
