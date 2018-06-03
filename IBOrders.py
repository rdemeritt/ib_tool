from ib_insync import util
import config
from utilities import whoami


def showAllOrders(_session):
    config.logger.debug(whoami())
    print(util.tree(_session.orders()))


def showWorkingOrders(_session):
    config.logger.debug(whoami())
    print(util.tree(_session.openOrders()))


def showFilledOrders(_session):
    config.logger.debug(whoami())
    print(util.tree(_session.fills()))

def showExecutions(_session):
    config.logger.debug(whoami())
    print(util.tree(_session.executions()))
