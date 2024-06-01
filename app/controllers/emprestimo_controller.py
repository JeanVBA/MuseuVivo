from flask import jsonify

from app.controllers.base_controller import base_controller
from app.services.emprestimo_service import EmprestimoService

emprestimo_service = EmprestimoService()
emprestimo_controller = base_controller(emprestimo_service)

def get_by_instituicao_name(instituicao_nome):
    result = emprestimo_service.fetch_by_instituicao_nome(instituicao_nome)
    if isinstance(result, dict):
        return jsonify(result)
    return result