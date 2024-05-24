from flask import Blueprint, request, jsonify, abort
from datetime import datetime
from app.models.emprestimo_model import Emprestimo
from app.models.obra_model import Obra
from app.views.emprestimo_view import emprestimo_to_dict, error_response
from app.extentions import db

emprestimo_bp = Blueprint('emprestimo_bp', __name__,url_prefix='/emprestimo')

@emprestimo_bp.route('/', methods=['GET'])
def get_emprestimos():
    emprestimos = Emprestimo.query.all()
    return jsonify([emprestimo_to_dict(emprestimo) for emprestimo in emprestimos])

@emprestimo_bp.route('/<int:id>', methods=['GET'])
def get_emprestimo(id):
    emprestimo = Emprestimo.query.get_or_404(id)
    return jsonify(emprestimo_to_dict(emprestimo))

@emprestimo_bp.route('/', methods=['POST'])
def create_emprestimo():
    data = request.get_json()
    emprestimo = Emprestimo(
        obra_id=data['obra_id'],
        data_emprestimo=data.get('data_emprestimo'),
        data_retorno=data.get('data_retorno'),
        instituicao_solicitante=data['instituicao_solicitante'],
    )
    if emprestimo.obra_id is None:
        return error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
    obra = Obra.query.get(emprestimo.obra_id)
    if obra is None:
        return error_response("Obra não localizada", 404)
    if emprestimo.data_retorno and datetime.fromisoformat(emprestimo.data_retorno) < datetime.now():
        return error_response("A data do retorno não pode ser antes da data atual", 400)
    if emprestimo.instituicao_solicitante is None:
        return error_response("Instituicao deve ser preenchida", 400)
    db.session.add(emprestimo)
    db.session.commit()
    return jsonify(emprestimo_to_dict(emprestimo)), 201

@emprestimo_bp.route('/<int:id>', methods=['PUT'])
def update_emprestimo(id):
    emprestimo = Emprestimo.query.get_or_404(id)
    data = request.get_json()
    emprestimo.obra_id = data.get('obra_id', emprestimo.obra_id)
    emprestimo.data_emprestimo = data.get('data_emprestimo', emprestimo.data_emprestimo)
    emprestimo.data_retorno = data.get('data_retorno', emprestimo.data_retorno)
    emprestimo.instituicao_solicitante = data.get('instituicao', emprestimo.instituicao_solicitante)
    if emprestimo.obra_id is None:
        return error_response("Não pode ser cadastrado sem ter associado uma obra", 400)
    obra = Obra.query.get(emprestimo.obra_id)
    if obra is None:
        return error_response("Obra não localizada", 404)
    if emprestimo.data_retorno and datetime.fromisoformat(emprestimo.data_retorno) < datetime.now():
        return error_response("A data do retorno não pode ser antes da data atual", 400)
    if emprestimo.instituicao_solicitante is None:
        return error_response("Instituicao deve ser preenchida", 400)
    db.session.commit()
    return jsonify(emprestimo_to_dict(emprestimo)), 200

@emprestimo_bp.route('/<int:id>', methods=['DELETE'])
def delete_emprestimo(id):
    autor = Emprestimo.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return '', 204