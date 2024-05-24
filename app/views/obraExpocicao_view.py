from flask import jsonify

def obraExposicao_to_dict(obra_exposicao):
    return {
        'obra_id': obra_exposicao.obra_id,
        'obra_nome': obra_exposicao.obra.nome,
        'exposicao_id': obra_exposicao.exposicao_id,
        'exposicao_titulo': obra_exposicao.exposicao.titulo
    }


def obrasExposicao_to_dict(obra_exposicao):
    return {
        'exposicao_id': obra_exposicao.exposicao_id,
        'exposicao_titulo': obra_exposicao.exposicao.titulo,
        'obra':
            {
                'id': obra_exposicao.obra.id,
                'nome': obra_exposicao.obra.nome,
                'autor': obra_exposicao.obra.autor.nome,
                'tipo': obra_exposicao.obra.tipo
            }

    }

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response