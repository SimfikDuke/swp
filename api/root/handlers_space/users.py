import datetime

from root import utils
from root.handlers_space import BaseHS
import root.db_models as models


class UsersHS(BaseHS):
    def login(self, login: str, password: str):
        user = self.session.query(models.User) \
            .filter(models.User.email == login) \
            .filter(models.User.password == password) \
            .first()
        if user is None:
            return None
        if user.token_updated_at < datetime.datetime.now() + datetime.timedelta(days=1):
            user.token = utils.generate_token()
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
