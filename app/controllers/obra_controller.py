from flask import Blueprint, request, jsonify, abort
from app.models.obra_model import Obra
from app.models.localizacao_model import Localizacao
from app.models.autor_model import Autor
from app.views.obra_view import obra_to_dict, error_response
from app.extentions import db

obra_bp = Blueprint('obra_bp', __name__,url_prefix='/obra')

@obra_bp.route('/', methods=['GET'])
def get_obras():
    obras = Obra.query.all()
    return jsonify([obra_to_dict(obra) for obra in obras])

@obra_bp.route('/<int:id>', methods=['GET'])
def get_obra(id):
    obra = Obra.query.get_or_404(id)
    return jsonify(obra_to_dict(obra))

@obra_bp.route('/', methods=['POST'])
def create_obra():
    data = request.json
    obra = Obra(
        nome=data['nome'],
        descricao=data.get('descricao'),
        data_criacao=data.get('data_criacao'),
        autor_id=data['autor_id'],
        localizacao_id=data['localizacao_id'],
        tipo=data.get('tipo')
    )
    if obra.tipo not in ['Escultura', 'Pintura']:
        return error_response('Tipo não encontrado, insira tipos válidos "Escultura ou Pintura".', 400)
    if obra.autor_id is None or not Autor.query.get(obra.autor_id):
        return error_response("Autor não localizado.", 400)
    if obra.localizacao_id is None or not Localizacao.query.get(obra.localizacao_id):
        return error_response("Localizao inexistente", 400)
    db.session.add(obra)
    db.session.commit()
    return jsonify(obra_to_dict(obra)), 201

@obra_bp.route('/<int:id>', methods=['PUT'])
def update_obra(id):
    obra = Obra.query.get_or_404(id)
    data = request.json
    obra.nome = data.get('nome', obra.nome)
    obra.descricao = data.get('descricao', obra.descricao)
    obra.data_criacao = data.get('data_criacao', obra.data_criacao)
    obra.autor_id = data.get('autor_id', obra.autor_id)
    obra.localizacao_id = data.get('localizacao_id', obra.localizacao_id)
    obra.tipo = data.get('tipo', obra.tipo)

    if obra.tipo not in ['Escultura', 'Pintura']:
       return error_response('Tipo não encontrado, insira tipos válidos "Escultura ou Pintura".', 400)
    if obra.autor_id is None:
        return error_response("Autor não pode ficar sem identificador.", 400)
    if obra.localizacao_id is None:
        return error_response("A obra precisa estar em uma localização.", 400)
    db.session.commit()
    return jsonify(obra_to_dict(obra))

@obra_bp.route('/<int:id>', methods=['DELETE'])
def delete_obra(id):
    obra = Obra.query.get_or_404(id)
    db.session.delete(obra)
    db.session.commit()
    return '', 204