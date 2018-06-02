from ib_insync import util

def showAllOrders(_session):
    print(util.tree(_session.orders()))


def showWorkingOrders(_session):
    print(util.tree(_session.openOrders()))


def showFilledOrders(_session):
    print(util.tree(_session.fills()))

def showExecutions(_session):
    print(util.tree(_session.executions()))
