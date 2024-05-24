from flask import Blueprint, request, jsonify, abort
from app.models.autor_model import Autor
from app.views.autor_view import autor_to_dict, error_response
from app.extentions import db

autor_bp = Blueprint('autor_bp', __name__,url_prefix='/autor')

@autor_bp.route('/', methods=['GET'])
def get_autores():
    autores = Autor.query.all()
    return jsonify([autor_to_dict(autor) for autor in autores])

@autor_bp.route('/<int:id>', methods=['GET'])
def get_autor(id):
    autor = Autor.query.get_or_404(id)
    return jsonify(autor_to_dict(autor))

@autor_bp.route('/', methods=['POST'])
def create_autor():
    data = request.get_json()
    autor = Autor(
        nome=data['nome']
    )
    if autor.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.add(autor)
    db.session.commit()
    return jsonify(autor_to_dict(autor)), 201

@autor_bp.route('/<int:id>', methods=['PUT'])
def update_autor(id):
    autor = Autor.query.get_or_404(id)
    data = request.get_json()
    autor.nome = data['nome']
    if autor.nome is None:
        return error_response("Campo nome deve ser preenchido", 400)
    db.session.commit()
    return jsonify(autor_to_dict(autor)), 200

@autor_bp.route('/<int:id>', methods=['DELETE'])
def delete_autor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return '', 204