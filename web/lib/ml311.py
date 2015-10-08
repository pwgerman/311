# Python 2.7 module for machine learning predictions for San Francisco 311

from datetime import datetime, timedelta
from pandas import Series, to_datetime
from time import sleep

def delta2sec(timedelta):
    """convert timedelta to seconds for calculations"""
    return Series(timedelta).astype('timedelta64[s]')

def sec2delta(time_sec):
    """Convert time in seconds to timedelta"""
    return timedelta(0, time_sec[0])
                
def predict(opendate, sup_dist=0):
    """Form a close date prediction as datetime object.

    Keyword arguments:
    opendate -- The case open date. {string or datetime}.
    sup_dist -- The case supervisor district. {int} (default 0 for none)
    """
    opendate = to_datetime(opendate)
    today = datetime.now()
    duration = delta2sec(today-opendate)
    return sec2delta(duration)


