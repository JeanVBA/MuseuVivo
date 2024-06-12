from flask import request, jsonify

from app.services.institution_service import InstitutionService
from app.controllers.base_controller import base_controller

institution_service = InstitutionService()
institution_controller = base_controller(institution_service)


def get_by_args():
    name = request.args.get('name')
    loan_name = request.args.get('loan_name')
    loan_date = request.args.get('loan_date')
    return_loan_date = request.args.get('return_loan_date')

    items = institution_service.fetch_by_args(name, loan_name, loan_date, return_loan_date)
    return jsonify(items)

