import datetime

from root import utils
from root.handlers_space import BaseHS
import root.db_models as models


class UsersHS(BaseHS):
    def login(self, login: str, password: str):
        user = self.session.query(models.User) \
            .filter(models.User.email == login) \
            .first()
        if user is None or user.password != password:
            return None
        if user.token_updated_at < datetime.datetime.now() - datetime.timedelta(days=1) or not user.token:
            user.token = utils.generate_token()
            user.token_updated_at = datetime.datetime.now()
        return user.token

    def register(self, name, login, password):
        exist = self.session.query(models.User) \
            .filter(models.User.email == login) \
            .count()
        if exist:
            return None
        user = models.User(name, login, password)
        self.session.add(user)
        user.token = utils.generate_token()
        return user.token
