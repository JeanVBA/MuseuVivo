from flask import jsonify


def ingresso_to_dict(ingresso):
    return {
        'id': ingresso.id,
        'tipo': ingresso.tipo,
        'data_visita': ingresso.data_visita,
        'visitante': {
            'nome': ingresso.visitante.nome
        },
        'visita_guiada': {
            'grupo': ingresso.visita_guiada.grupo,
            'guia': {
                'nome': ingresso.visita_guiada.guia.nome
            }
        }
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response