from ib_insync import util


def showOpenTrades(_session):
    print(util.tree(_session.openTrades()))

def showTrades(_session):
    print(util.tree(_session.trades()))
