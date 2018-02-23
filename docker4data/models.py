from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class QueryHistory(db.Model):
    __tablename__ = 'query_history'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    result = db.Column(db.String)
    processed = db.Column(db.Boolean, default=False)

    date_created = db.Column(
        db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<QueryHistory %r>' % self.id
