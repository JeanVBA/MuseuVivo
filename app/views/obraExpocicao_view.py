from flask import jsonify


def obra_exposicao_to_dict(obra_exposicao):
    return {
        'obra_id': obra_exposicao.obra_id,
        'exposicao_id': obra_exposicao.exposicao_id,
        'obra_nome': obra_exposicao.obra.nome,
        'exposicao_titulo': obra_exposicao.exposicao.titulo
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response