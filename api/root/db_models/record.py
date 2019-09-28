import datetime

from sqlalchemy import orm

import root.db_models as models
import sqlalchemy as sa


class Record(models.Base):
    __tablename__ = 'records'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    title = sa.Column(sa.String, nullable=False)
    text = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.datetime.now)

    user: 'models.User' = orm.relationship('User', back_populates='records')

    def __init__(self, user_id: int, title: str, text: str):
        self.user_id = user_id
        self.title = title
        self.text = text

    def to_web(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'text': self.text,
            'author': self.user.name,
            'created_at': self.created_at.strftime('%H:%M  %d %h'),
        }
