import os
from os import path
from typing import Dict, Any
import yaml
from root.enums import DBConfig


class Context:

    def __init__(self):
        self.project_path = path.dirname(path.dirname(path.realpath(__file__)))
        self.static_path = os.path.join(self.project_path, 'static')
        with open(path.join(self.project_path, 'config.yaml'), 'r') as f:
            self.config: Dict[str, Any] = yaml.safe_load(f)
        self.site_url = self.config.get('site_url', 'localhost:5000')
        db = self.config['db']
        self.db_config = DBConfig(db['server'], db['port'], db['name'], db['login'], db['password'])
        self.db_con_string = f'postgres://{self.db_config.login}:{self.db_config.password}@{self.db_config.server}:' \
            f'{self.db_config.port}/{self.db_config.name}'
