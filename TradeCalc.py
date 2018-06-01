import config
import math

r_value = 100

def calcEntryStop(_entry, _stop, _r_value=r_value):
    # going long or short
    if _entry > _stop:
        is_bear = False
        is_bull = True
    elif _entry < _stop:
        is_bear = True
        is_bull = False
    else:
        config.logger.error('entry and stop values must be different')
        return False

