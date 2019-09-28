from abc import ABC

from sqlalchemy.orm import Session

import root.db_models as models


class BaseHS(ABC):
    request = None
    session = None
    user: models.User = None

    def __init__(self, request, session: Session, user: models.User):
        self.request = request
        self.session = session
        self.user = user
