import config
import math

r_value = 100

def calcEntryStopShares(_entry_stop, _r_value=r_value):
    def parseEntryStop(__es_string):
        # strip away any whitespaces
        __es_string.replace(' ', '')

        if ':' in __es_string.split('x')[0]:
            stp = __es_string.split('x')[0].split(':')[0]
            lmt = __es_string.split('x')[0].split(':')[1]
        else:
            stp = __es_string.split('x')[0]
            lmt = __es_string.split('x')[0]

        __es_dict = {
            'entry': {
                'stp': float(stp),
                'lmt': float(lmt)
            },
            'stop': float(__es_string.split('x')[1])
        }
        return __es_dict

    def calc_risk(__entry, __stop):
        return round(abs(__entry - __stop), 2)

    def calc_shares(__risk, __r_value):
        return int(__r_value / __risk)

    config.logger.debug(f'calculating {_entry_stop} with {_r_value} R')
    es_dict = parseEntryStop(_entry_stop)

    ess_dict = {
        'r_value': _r_value,
        'entry': {
            'stp': es_dict['entry']['stp'],
            'lmt': es_dict['entry']['lmt']
        },
        'stop': es_dict['stop'],
        'shares': None,
        'risk': calc_risk(es_dict['entry']['lmt'], es_dict['stop'])
    }

    entry = ess_dict['entry']['lmt']
    stop = ess_dict['stop']

    # going long or short?
    if entry > stop:
        ess_dict['shares'] = calc_shares(ess_dict['risk'], ess_dict['r_value'])
    elif entry < stop:
        ess_dict['shares'] = (calc_shares(ess_dict['risk'], ess_dict['r_value']) * -1)
    else:
        config.logger.error('we have a problem')
        return False

    return ess_dict
