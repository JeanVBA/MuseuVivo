from flask import jsonify


def emprestimo_to_dict(emprestimo):
    return {
        'id': emprestimo.id,
        'obra': {
            'id': emprestimo.obra.id,
            'nome': emprestimo.obra.nome,
            'descricao': emprestimo.obra.descricao,
            'data_criacao': emprestimo.obra.data_criacao,
            'autor': emprestimo.obra.autor.nome if emprestimo.obra.autor else None,
            'localizacao': emprestimo.obra.localizacao.nome if emprestimo.obra.localizacao else None,
            'tipo': emprestimo.obra.tipo
        },
        'data_emprestimo': emprestimo.data_emprestimo,
        'data_retorno': emprestimo.data_retorno,
        'instituicao': emprestimo.instituicao_solicitante
    }

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response