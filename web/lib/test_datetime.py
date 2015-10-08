# testing of functions in ml311 module

from ml311 import *

from time import sleep

t0 = datetime(2015, 10, 05)

t1 = datetime.now()

t1-t0

print sec2delta(delta2sec(t1-t0))

data_opened = '08/05/2015 12:54:03 AM'

print predict(data_opened)
