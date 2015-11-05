# plot 311 data


import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# create plots inline in notebook
%matplotlib inline   
import ml311


raw_data = '/Users/walter/Data/SF/Case_Data_from_San_Francisco_311__SF311_2015-10-22.csv'
outputfilename = raw_data.strip('.cvs')+'proc.csv'


