from ib_insync import util
import pandas as pd

def showPositions(_session):
    print(util.tree(_session.portfolio())[0][1])
