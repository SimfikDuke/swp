from typing import Any

from sqlalchemy.orm import Session
from tornado import escape
from tornado.escape import json_decode
from tornado.template import Loader
from tornado.web import RequestHandler

from root import context, engine
import root.db_models as models
import root.handlers_space as hs
import root.utils as utils
from root.utils import JsonArgs
import root.enums as enums


class BaseHandler(RequestHandler):
    session = Session(engine, expire_on_commit=False)
    json_args: JsonArgs = JsonArgs({})
    records: hs.RecordsHS
    users: hs.UsersHS
    user = None

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def data_received(self, chunk):
        """Overload of not implemented method to avoid pep8 linter warnings"""

    def get(self, *args, **kwargs):
        self.write('Not implemented')

    def post(self, *args, **kwargs):
        self.write('Not implemented')

    def put(self, *args, **kwargs):
        self.write('Not implemented')

    def delete(self, *args, **kwargs):
        self.write('Not implemented')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

    def prepare(self):
        content_type = self.request.headers.get('Content-Type', '')
        if any((i in content_type for i in ('application/x-json', 'application/json'))):
            # if self.request.headers.get('Content-Type') in ('application/x-json', 'application/json'):
            self.json_args = JsonArgs(json_decode(self.request.body) if self.request.body else {})
            self.json_args.finish_method = self.send_json
        elif 'multipart/form-data' in content_type:
            print(self.request.files)
        else:  # self.request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
            for k, v in self.request.arguments.items():
                if len(v) == 1:
                    self.json_args[k] = v[0].decode('utf-8')
                elif len(v) > 1:
                    self.json_args[k] = [v[i].decode('utf-8') for i in range(len(v))]
        self.identify_user()
        self.init_hs()
        self.json_args.finish_method = self.send_json

    def on_finish(self):
        self.session.commit()
        self.session.close()

    def send_json(self, data, status=200) -> None:
        self.set_header('Content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_status(status)
        self.finish(escape.json_encode(data))

    def init_hs(self):
        self.records = hs.RecordsHS(self, self.session)
        self.users = hs.UsersHS(self, self.session)

    def send_ok(self):
        ok_data = {
            'msg': 'ok'
        }
        self.send_json(ok_data)

    def send_failed(self):
        ok_data = {
            'msg': 'failed'
        }
        self.send_json(ok_data, 400)

    def write_error(self, status_code: int, **kwargs: Any):
        exc = kwargs['exc_info'][1]
        self.send_json(f'Error. {exc}', status_code)

    def identify_user(self):
        token = self.request.headers.get('Authorization')
        if token is None:
            self.user = None
        user = self.session.query(models.User) \
            .filter(models.User.token == token).first()
        self.user = user


class RecordsHandler(BaseHandler):
    def get(self):
        records = self.session.query(models.Record).all()
        self.send_json({'data': utils.to_web(records)})

    def post(self):
        if self.user and self.user.role == enums.UserRole.Admin.value:
            title = self.json_args['title']
            text = self.json_args['text']
            self.records.add_record(title, text)
            self.send_ok()
        else:
            self.send_failed()


class LoginHandler(BaseHandler):
    def post(self):
        login = self.json_args['login']
        password = self.json_args['password']
        token = self.users.login(login, password)
        if token:
            self.send_json({'token': token})
        else:
            self.send_failed()


class RegisterHandler(BaseHandler):
    def post(self):
        name = self.json_args['name']
        login = self.json_args['login']
        password = self.json_args['password']
        token = self.users.register(name, login, password)
        if token:
            self.send_json({'token': token})
        else:
            self.send_failed()

    def get(self):
        self.send_ok()
