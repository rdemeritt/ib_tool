from ib_insync import util


def showOpenTrades(_session):
    print(util.df(_session.openTrades()))
