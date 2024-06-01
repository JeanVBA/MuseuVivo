from datetime import datetime, time

from app.models.guia_model import Guia
from app.services.base_service import BaseService
from app.repositories.visitaGuiada_repository import VisitaGuiadaRepository

class VisitaGuiadaService(BaseService):
    def __init__(self):
        super().__init__(VisitaGuiadaRepository())

    def to_dict(self, visitas_guiadas):
        return {
            'id': visitas_guiadas.id,
            'grupo': visitas_guiadas.grupo,
            'data_visita': visitas_guiadas.data_visita,
            'horario': visitas_guiadas.horario.strftime('%H:%M:%S'),
            'guia': {
                'nome': visitas_guiadas.guia.nome if visitas_guiadas.guia is not None else None,
            }
        }

    def create(self, data):
        visitaGuiada_data = {
            'grupo': data.get('grupo'),
            'data_visita': data.get('data_visita'),
            'horario': data.get('horario'),
            'guia_responsavel_id': data['guia_responsavel_id']
        }
        if visitaGuiada_data['guia_responsavel_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter alocado um guia", 400)
        guia = Guia.query.get(visitaGuiada_data['guia_responsavel_id'])
        if guia is None:
            return self.error_response("Guia não encontrado", 404)
        if visitaGuiada_data['data_visita'] is None or datetime.fromisoformat(visitaGuiada_data['data_visita']) < datetime.now():
            return self.error_response("A data da visita não pode ser antes da data atual", 400)
        if visitaGuiada_data['horario'] is None:
            return self.error_response("O horario deve estar entre 09h à 17h")
        if visitaGuiada_data['horario']:
            horario_visita = datetime.strptime(visitaGuiada_data['horario'], '%H:%M').time()
            inicio_horario = time(9, 0)
            fim_horario = time(17, 0)
            if not (inicio_horario <= horario_visita <= fim_horario):
                return self.error_response("O horário da visita deve estar entre 09h e 17h", 400)
        instance = self.repository.create(**visitaGuiada_data)
        return self.to_dict(instance)

    def update(self, id, data):
        visitaGuiada = self.repository.get_by_id(id)
        visitaGuiada_data = {
            'grupo': data.get('grupo'),
            'data_visita': data.get('data_visita'),
            'horario': data.get('horario'),
            'guia_responsavel_id': data['guia_responsavel_id']
        }
        if visitaGuiada_data['guia_responsavel_id'] is None:
            return self.error_response("Não pode ser cadastrado sem ter alocado um guia", 400)
        guia = Guia.query.get(visitaGuiada_data['guia_responsavel_id'])
        if guia is None:
            return self.error_response("Guia não encontrado", 404)
        if visitaGuiada_data['data_visita'] is None or datetime.fromisoformat(
                visitaGuiada_data['data_visita']) < datetime.now():
            return self.error_response("A data da visita não pode ser antes da data atual", 400)
        if visitaGuiada_data['horario'] is None:
            return self.error_response("O horario deve estar entre 09h à 17h")
        if visitaGuiada_data['horario']:
            horario_visita = datetime.strptime(visitaGuiada_data['horario'], '%H:%M').time()
            inicio_horario = time(9, 0)
            fim_horario = time(17, 0)
            if not (inicio_horario <= horario_visita <= fim_horario):
                return self.error_response("O horário da visita deve estar entre 09h e 17h", 400)
        instance = self.repository.update(visitaGuiada, **visitaGuiada_data)
        return self.to_dict(instance)

    def fetch_by_id(self, id):
        try:
            instance = self.repository.get_by_id(id)
            return self.to_dict(instance)
        except Exception as e:
            return self.error_response("VisitaGuiada não encontrado", 404)

    def delete(self, id):
        try:
            instance = self.repository.get_by_id(id)
            self.repository.delete(instance)
        except Exception as e:
            return self.error_response("VisitaGuiada não encontrado", 404)
