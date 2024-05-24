from flask import jsonify


def exposicao_to_dict(exposicao):
    return {
        'id': exposicao.id,
        'titulo': exposicao.titulo,
        'descricao': exposicao.descricao,
        'data_inicio': exposicao.data_inicio,
        'data_termino': exposicao.data_termino
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response