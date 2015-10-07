# Python 2.7 module for machine learning predictions for San Francisco 311

from datetime import datetime
from pandas import to_datetime

def predict(opendate, sup_dist=0):
    """Form a close date prediction as datetime object.

    Keyword arguments:
    opendate -- The case open date. {string or datetime}.
    sup_dist -- The case supervisor district. {int} (default 0 for none)
    """
    opendate = to_datetime(opendate)
    return datetime.now()

def helloworld():
    print 'Hello world'

