from ib_insync import util
import pandas as pd
from cmd2 import Cmd

def showPositions(_session):
    #print(util.tree(_session.portfolio()))

    for contract in util.tree(_session.portfolio()):
        #print(contract)
        # unrealized gain
        urg = Cmd().colorize(str(contract[5]), posneg(contract[5]))
        tick = contract[0]['Contract']['symbol']
        pos = Cmd().colorize(str(contract[1]), posneg(contract[1]))
        mval = contract[3]
        avp = contract[4]
        last = round(contract[2], 2)

        print(f'{urg}\t{tick}\t{pos}\t{mval}\t{avp}\t{last}')

def posneg(_value):
    if _value > 0:
        return 'green'
    if _value < 0:
        return 'red'
    else:
        return 'bold'
