from flask import jsonify


def seguranca_to_dict(seguranca):
    return {
        'id': seguranca.id,
        'nome': seguranca.nome,
        'email': seguranca.email,
        'telefone': seguranca.telefone,
        'localizacao': {
            'nome': seguranca.localizacao.nome,
        }
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response