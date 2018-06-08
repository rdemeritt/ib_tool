import argparse
import re
from utilities import unix_time_now
from log import build_logger, logging
from ib_insync import IB
from IBConnector import IBConnector


def build_arg_parser():
    parser = argparse.ArgumentParser(prog='ibsh', description='CLI tool to place and manage orders in IB')
    parser.add_argument('--log_level', help='Set the logging level')
    return parser.parse_args()


def init():
    global session
    global start_time
    global logger
    global args

    start_time = unix_time_now()
    args = build_arg_parser()

    if args.log_level:
        global log_level
        log_level = getattr(logging, args.log_level.upper())
    logger = build_logger()

    ib_conn = IBConnector()
    session = ib_conn.start_session()

    if not session:
        exit(2)


# define global variables
start_time = None
logger = None
log_level = logging.WARN
args = None
session = None
