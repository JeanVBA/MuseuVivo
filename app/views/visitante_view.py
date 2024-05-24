from flask import jsonify


def visitante_to_dict(visitante):
    return{
        "id": visitante.id,
        'nome': visitante.nome,
        'email': visitante.email,
        'telefone': visitante.telefone
    }

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response