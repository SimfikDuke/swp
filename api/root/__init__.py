import logging

from root.context import Context
from sqlalchemy import create_engine

logging.basicConfig(format=f'[%(name)s] %(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

context = Context()
logger.info(f'Context initialized.')

engine = create_engine(context.db_con_string, echo=False)
logger.info(f'Connected to DB {context.db_config.server} successfully.')

