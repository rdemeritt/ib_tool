from ib_insync import util

def showAccountSummary(_session):
    print(util.df(_session.accountSummary()))

def showAccountValues(_session):
    print(util.df(_session.accountValues()))
