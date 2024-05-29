from app.models.visitaGuiada_model import VisitaGuiada
from app.models.visitante_model import Visitante
from app.services.base_service import BaseService
from app.repositories.ingresso_repository import IngressoRepository
from datetime import datetime


class IngressoService(BaseService):
    def __init__(self):
        super().__init__(IngressoRepository())

    def to_dict(self, ingresso):
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

    def create(self, data):
        ingresso_data = {
            'visitante_id': data.get('visitante_id'),
            'tipo': data.get('tipo'),
            'data_visita': data.get('data_visita'),
            'visita_guiada_id': data.get('visita_guiada_id')
        }
        if ingresso_data['visitante_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado um visitante", 400)
        visitante = Visitante.query.get(ingresso_data['visitante_id'])
        if visitante is None:
            return self.error_response("Visitante não localizada", 404)
        if ingresso_data['tipo'] not in ['Silver', 'Gold', 'Premium']:
            return self.error_response("O tipo do ingresso deve ser 'Silver, Gold ou Premium'", 400)
        if ingresso_data['data_visita'] and datetime.fromisoformat(ingresso_data['data_visita']) < datetime.now():
            return self.error_response("A data do visita não pode ser antes da data atual", 400)
        if ingresso_data['visita_guiada_id'] is None:
            return self.error_response("Instituicao deve ser preenchida", 400)
        visitaGuiada = VisitaGuiada.query.get(ingresso_data['visita_guiada_id'])
        if visitaGuiada is None:
            return self.error_response("VisitaGuiada não localizada", 404)
        instance = self.repository.create(**ingresso_data)
        return self.to_dict(instance)

    def update(self, id, data):
        ingresso = self.repository.get_by_id(id)
        ingresso_data = {
            'visitante_id': data.get('visitante_id'),
            'tipo': data.get('tipo'),
            'data_visita': data.get('data_visita'),
            'visita_guiada_id': data.get('visita_guiada_id')
        }
        if ingresso_data['visitante_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter associado um visitante", 400)
        visitante = Visitante.query.get(ingresso_data['visitante_id'])
        if visitante is None:
            return self.error_response("Visitante não localizada", 404)
        if ingresso_data['tipo'] not in ['Silver', 'Gold', 'Premium']:
            return self.error_response("O tipo do ingresso deve ser 'Silver, Gold ou Premium'", 400)
        if ingresso_data['data_visita'] and datetime.fromisoformat(ingresso_data['data_visita']) < datetime.now():
            return self.error_response("A data do visita não pode ser antes da data atual", 400)
        if ingresso_data['visita_guiada_id'] is None:
            return self.error_response("Instituicao deve ser preenchida", 400)
        visitaGuiada = VisitaGuiada.query.get(ingresso_data['visita_guiada_id'])
        if visitaGuiada is None:
            return self.error_response("VisitaGuiada não localizada", 404)
        instance = self.repository.update(ingresso, **ingresso_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            instance = self.repository.get_by_id(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Ingresso não encontrado", 404)

    def delete(self, id):
        try:
            instance = self.repository.query.get(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("Ingresso não encontrado", 404)
