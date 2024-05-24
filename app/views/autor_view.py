from flask import jsonify


def autor_to_dict(Autor):
    return {
        'id': Autor.id,
        'nome': Autor.nome,
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response