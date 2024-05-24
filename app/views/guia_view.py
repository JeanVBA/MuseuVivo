from flask import jsonify


def guia_to_dict(guia):
    return {
        'id': guia.id,
        'nome': guia.nome,
        'email': guia.email,
        'telefone': guia.telefone
    }

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response
