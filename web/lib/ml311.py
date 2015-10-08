# Python 2.7 module for machine learning predictions for San Francisco 311

from datetime import datetime, timedelta
from pandas import Series, to_datetime, Timedelta
from time import sleep

def delta2sec(timedelta):
    """convert timedelta to seconds for calculations"""
    return Series(timedelta).astype('timedelta64[s]')

def sec2delta(time_sec):
    """Convert time in seconds to timedelta"""
    return timedelta(0, time_sec[0])
                
dist_mean = {0: Timedelta('43 days 10:05:11.056561'),
    1: Timedelta('31 days 03:01:06.400110'),
    2: Timedelta('35 days 18:07:55.616361'),
    3: Timedelta('30 days 12:57:33.091409'),
    4: Timedelta('25 days 11:48:10.053727'),
    5: Timedelta('33 days 14:24:03.329275'),
    6: Timedelta('29 days 01:48:47.504794'),
    7: Timedelta('36 days 20:50:12.719682'),
    8: Timedelta('34 days 08:18:10.018732'),
    9: Timedelta('30 days 11:13:43.305337'),
    10: Timedelta('44 days 22:47:57.477616'),
    11: Timedelta('30 days 01:33:16.452858')}

def predict(opendate, sup_dist=5):
    """Form a close date prediction as datetime object.

    Keyword arguments:
    opendate -- The case open date. {string or datetime}.
    sup_dist -- The case supervisor district. {int} (default 0 for none)
    """
    opendate = to_datetime(opendate)
    today = datetime.now()
    duration = delta2sec(today-opendate)
    model_mean = timedelta(days=33)
    return dist_mean[sup_dist]
#    return sec2delta(duration)
#    return model_mean


