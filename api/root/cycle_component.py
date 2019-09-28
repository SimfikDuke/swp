import datetime
import logging
import time
from threading import Thread
from typing import Optional, Callable, Union


class CycleComponent:
    def __init__(self, period: Optional[float], body: Callable[..., Union[bool, float]], name: str,
                 execute_at: Optional[datetime.time] = None, wait: Optional[datetime.timedelta] = None):
        self.period = period
        self.body = body
        self.enabled = True
        if execute_at is None:
            self.next_body_execute_at = datetime.datetime.now()
        else:
            first_execute = datetime.datetime.combine(datetime.date.today(), execute_at)
            while first_execute < datetime.datetime.now():
                first_execute += datetime.timedelta(seconds=period)
            self.next_body_execute_at = first_execute
        if wait:
            self.next_body_execute_at += wait
        self.logger = logging.getLogger(name)
        self.__t = Thread(target=self.__loop)
        self.__t.start()

    def __loop(self):
        self.logger.debug('CycleComponent started.')
        dont_stop = True
        while self.enabled and dont_stop:
            # noinspection PyBroadException
            try:
                now = datetime.datetime.now()
                if self.next_body_execute_at <= now:
                    body_result = self.body()
                    if type(body_result) is bool:
                        dont_stop = body_result
                        if self.period is not None:
                            self.next_body_execute_at = now + datetime.timedelta(seconds=self.period)
                    elif type(body_result) is float:
                        self.next_body_execute_at = now + datetime.timedelta(seconds=body_result)
                    else:
                        raise Exception(f'Bad body() return type: {type(body_result)} (must be bool or float).')
            except BaseException as ex:
                dont_stop = False
                self.logger.exception('CycleComponent exception.', exc_info=ex)
            time.sleep(.1)
        self.enabled = False
        self.logger.info('CycleComponent stopped.')

    def stop(self):
        self.enabled = False
        self.__t.join()

    def join(self):
        self.__t.join()

    def is_alive(self) -> bool:
        return self.__t.is_alive()
