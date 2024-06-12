from flask import jsonify, request

from app.controllers.base_controller import base_controller
from app.services.loan_service import LoanService

loan_service = LoanService()
loan_controller = base_controller(loan_service)

def get_by_institution_name(institution_name):
    result = loan_service.fetch_by_institution_name(institution_name)
    if isinstance(result, dict):
        return jsonify(result)
    return result

def get_by_work_of_art_name(work_of_art_name):
    result = loan_service.fetch_by_work_of_art_name(work_of_art_name)
    if isinstance(result, dict):
        return jsonify(result)
    return result

def get_by_args():
    return_date = request.args.get('return_date')
    loan_date = request.args.get('loan_date')
    work_of_art_name = request.args.get('work_of_art_name')
    institution_name = request.args.get('institution_name')

    items = loan_service.fetch_by_args(return_date, loan_date, work_of_art_name, institution_name)
    return jsonify(items)