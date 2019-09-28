import logging

import tornado.ioloop
import tornado.web

from root.handlers import *
import root

logger = logging.getLogger(__name__)


def make_app():
    settings = {
        'static_path': context.static_path
    }
    return tornado.web.Application([
        (r"/records", RecordsHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    logger.info('Application started')
    tornado.ioloop.IOLoop.current().start()
