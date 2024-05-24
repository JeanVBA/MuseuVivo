from flask import jsonify


def obra_to_dict(obra):
    obra_dict = {
        'id': obra.id,
        'nome': obra.nome,
        'descricao': obra.descricao,
        'data_criacao': obra.data_criacao,
        'autor': obra.autor.nome if obra.autor else None,
        'localizacao': obra.localizacao.nome if obra.localizacao else None,
        'tipo': obra.tipo
    }
    if obra.tipo == 'Escultura' and obra.escultura:
        obra_dict['escultura'] = {
            'material': obra.escultura.material,
            'peso': obra.escultura.peso
        }
    elif obra.tipo == 'Pintura' and obra.pintura:
        obra_dict['pintura'] = {
            'tecnica': obra.pintura.tecnica
        }
    return obra_dict

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response