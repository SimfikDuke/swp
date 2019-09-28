import logging
import os
import random
from contextlib import contextmanager
from typing import Any, List

from sqlalchemy.orm import Session

from root import context, engine
logger = logging.getLogger(__name__)


class JsonArgs(dict):
    finish_method = None

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except Exception as e:
            self.finish_method(f'Expected argument [{item}] but not represent.', 400)


def is_pid_exists(name: str):
    pid_file_path = os.path.join(context.project_path, 'pids', f'{name}.pid')
    return os.path.isfile(pid_file_path)


def make_pid(name, pid):
    pid_file_path = os.path.join(context.project_path, 'pids', f'{name}.pid')
    with open(pid_file_path, 'w+') as pid_file:
        pid_file.write('{}\n'.format(pid))
        pid_file.close()
    return True


@contextmanager
def sess(auto_commit=True) -> Session:
    session = Session(engine)
    try:
        yield session
    finally:
        if auto_commit:
            session.commit()
        session.close()


def to_web(items: List[Any], **kwargs):
    return list(map(lambda item: item.to_web(**kwargs), items))


def generate_token():
    return ''.join((chr(65 + random.choice(range(26))) for _ in range(24)))
