from ib_insync import util
from cmd2 import Cmd


def showPositions(_session):
    for position in util.tree(_session.portfolio()):
        pdict = parsePosition(position)

        urg = pdict['urg']
        tick = pdict['tick']
        size = pdict['size']
        mval = pdict['mval']
        avsp = pdict['avsp']
        last = pdict['last']

        print(f'{urg:>7}\t{tick}\t{size:5}\t{mval:>12,}\t{avsp:>10,}\t{last:>10,}')


def posneg(_value):
    if _value > 0:
        return 'green'
    if _value < 0:
        return 'red'
    else:
        return 'bold'


def parsePosition(_position):
    # unrealized gain
    urg = Cmd().colorize(str(_position[5]), posneg(_position[5]))
    tick = _position[0]['Contract']['symbol']
    size = Cmd().colorize(str(_position[1]), posneg(_position[1]))
    # market vale
    mval = _position[3]
    # average price per share
    avsp = _position[4]
    last = round(_position[2], 2)

    position = {
        'urg': urg,
        'tick': tick,
        'size': size,
        'mval': mval,
        'avsp': avsp,
        'last': last
    }
    return position


def showPNL(_session):
    print(util.tree(_session.pnl()))


# don't need this one... just keeping it around to remind myself
# that positions() isn't any better than portfolio()
def showPosPos(_session):
    print(util.tree(_session.positions()))
