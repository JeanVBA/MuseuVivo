from flask import jsonify


def escultura_to_dict(escultura):
    return {
        'id': escultura.id,
        'obra_id': escultura.obra_id,
        'material': escultura.material,
        'peso': escultura.peso,
        'obra': {
            'id': escultura.obra.id,
            'nome': escultura.obra.nome,
            'descricao': escultura.obra.descricao,
            'data_criacao': escultura.obra.data_criacao,
            'autor': escultura.obra.autor.nome if escultura.obra.autor else None,
            'localizacao': escultura.obra.localizacao.nome if escultura.obra.localizacao else None,
            'tipo': escultura.obra.tipo
        }
    }


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response
