import logging
from rd_utilities import unix_time_now


def build_logger():
    logger_name = 'ib_tool'
    formatter = logging.Formatter("[%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:%(filename)s(%(lineno)s)] "
                                  "%(message)s", "%Y-%m-%dT%H:%M:%S")
    _logger = logging.getLogger(logger_name)

    # log to file
    fh = logging.FileHandler('%s_%s.log' % (logger_name, unix_time_now()))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # log to the console as well
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=(fh, ch))
    return _logger