import argparse
import re
from utilities import unix_time_now
from log import build_logger, logging
from ib_insync import IB


def build_arg_parser():
    parser = argparse.ArgumentParser(
        prog='ibsh', description='CLI tool to place and manage orders in IB')
    # parser.add_argument('--broker', '-b', help='Which broker to connect to', required=True)
    parser.add_argument('--log_level', help='Set the logging level')
    # parser.add_argument('--key', help='IB API key', required=True)
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

    # # process our arguments
    # if args.key:
    #     pass
    # # drop out if we don't have a way to setup session
    # else:
    #     logger.error('No key provided')
    #     exit(1)

    session = IB().connect()
    # check to see if our session was successfully created
    if not session:
        exit(2)


# define global variables
start_time = None
logger = None
log_level = logging.DEBUG
args = None
session = None
