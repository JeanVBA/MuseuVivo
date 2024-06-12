from app.extentions import db


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'))
    type = db.Column(db.String(10))
    visit_date = db.Column(db.Date)
    guided_visit_id = db.Column(db.Integer, db.ForeignKey('guided_visits.id'))
    visitor = db.relationship('Visitor', backref=db.backref('tickets', lazy=True))
    guided_visit = db.relationship('GuidedVisit', backref=db.backref('tickets', lazy=True))