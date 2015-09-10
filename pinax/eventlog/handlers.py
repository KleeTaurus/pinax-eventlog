import logging

from .models import Log as model


class DBHandler(logging.Handler):

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        log_entry = model(user=None,
                          action=record.levelname,
                          extra={'pathname': record.pathname,
                                 'lineno': record.lineno,
                                 'message': record.getMessage()})
        log_entry.save()
