import datetime
from typing import Any, Dict, List

from sqlalchemy import orm

import root.db_models as models
import sqlalchemy as sa
import sqlalchemy_utils.types.password as pwd


class User(models.Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    email = sa.Column(sa.String, unique=True, nullable=False)
    password = sa.Column(pwd.PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))
    token = sa.Column(sa.String)
    token_updated_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    role = sa.Column(sa.SmallInteger, nullable=False, default=0, server_default='0')
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)

    records: List['models.Record'] = orm.relationship('Record', back_populates='user')

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def to_web(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at,
        }
