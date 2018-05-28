import  config

def showAllOrders(_session):
    print(_session.orders())


def showWorkingOrders(_session):
    print(_session.openOrders())


def showFilledOrders(_session):
    print(_session.fills())
