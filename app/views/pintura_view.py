from flask import jsonify


def pintura_to_dict(Pintura):
    return dict(id=Pintura.id, obra_id=Pintura.obra_id, tecnica=Pintura.tecnica, obra={
        'id': Pintura.obra.id,
        'nome': Pintura.obra.nome,
        'descricao': Pintura.obra.descricao,
        'data_criacao': Pintura.obra.data_criacao,
        'autor': Pintura.obra.autor.nome if Pintura.obra.autor else None,
        'localizacao': Pintura.obra.localizacao.nome if Pintura.obra.localizacao else None,
    })


def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response