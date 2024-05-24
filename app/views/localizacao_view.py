from flask import jsonify


def localizacao_to_dict(localizacao):
    return {
        'nome': localizacao.nome
    }
def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response