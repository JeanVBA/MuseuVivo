from flask import jsonify


def visitasGuiadas_to_dict(visitas_guiadas):
    return {
        'id': visitas_guiadas.id,
        'grupo': visitas_guiadas.grupo,
        'nombre': visitas_guiadas.nombre,
        'data_visita': visitas_guiadas.data_visita,
        'horario': visitas_guiadas.horario,
        'guia': {
            'nome': visitas_guiadas.guia.nome,
        }
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response