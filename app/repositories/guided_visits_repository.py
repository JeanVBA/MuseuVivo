from app.repositories.base_repository import BaseRepository
from app.models.guided_visits_model import GuidedVisit


class GuidedVisitRepository(BaseRepository):
    def __init__(self):
        super().__init__(GuidedVisit)

    def get_by_args(self, group=None, visit_date=None, hours=None, responsible_guide_name=None):
        query = GuidedVisit.query
        if group:
            query = query.filter(GuidedVisit.group.ilike(f'%{group}%'))
        if visit_date:
            query = query.filter(GuidedVisit.visit_date == visit_date)
        if hours:
            query = query.filter(GuidedVisit.hours == hours)
        if responsible_guide_name:
            query = query.filter(GuidedVisit.guide.name.ilike(f'%{responsible_guide_name}%'))
        return query.all()
