from app.extentions import db


class GuidedVisit(db.Model):
    __tablename__ = 'guided_visits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group = db.Column(db.String(255))
    visit_date = db.Column(db.Date)
    hours = db.Column(db.Time)
    responsible_guide_id = db.Column(db.Integer, db.ForeignKey('guides.id'))
    guide = db.relationship('Guide', backref=db.backref('guided_visits', lazy=True))
