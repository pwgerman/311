# Python 2.7 module for machine learning predictions for San Francisco 311
"""Module Docstring
Functions:  
load_data()  
save_data()
process_timedelta()
process_datetime()
delta2sec()
sec2delta()
predict()

Intended use in ipython:
raw_data = '/Users/walter/Data/SF/Case_Data_from_San_Francisco_311__SF311_2015-10-13.csv'
%time df = ml311.load_data(raw_data)
import sys    # optional
sys.stdout.flush()    #optional
%time df = ml311.process_datetime(df)
outputfilename = raw_data.strip('.cvs')+'proc.csv'
ml311.save_data(df, outputfilename)
# when reloading
%time df = ml311.load_data(outputfilename)
# when analyzing
%time df = ml311.process_timedelta(df)
"""

from datetime import datetime, timedelta
from pandas import Series, to_datetime, Timedelta
import pandas as pd
from time import sleep
import sys

dist_names = ['None', 'Richmond','Marina', 'North Beach to Market', 'Sunset', \
            'Panhandle', 'Soma to Tenderloin', 'West Portal to Merced', \
            'Noe Valley', 'Mission to Bernal', 'Bay View', 'Excelsior']

def load_data(filename):
    """load a saved datafile with datetime conversion for times
    RETURNS a pandas DataFrame of the csv file from 311.
    Designed for either raw file from 311 or processed file with datetime
    converted."""
    ## Loading a CSV file, without a header (so we have to provide field names)
    df = pd.read_csv(filename, index_col=0)  

    # if ml311.process_datetimes has already been and saved, then read as
    # datetimes.
    if 'Opened_dt' in df.columns:
        df['Opened_dt']=pd.to_datetime(df['Opened_dt'])
    if 'Closed_dt' in df.columns:
        df['Closed_dt']=pd.to_datetime(df['Closed_dt'])

    return df
    
def save_data(df, newfilename):
    """This will save datafiles in a format for datetimes to be read in more
    quickly."""
    # if 'Opened_dt' in df.columns ... convert to str
   # if 'Opened_dt in columns'
    if 'Opened_dt' in df.columns:
        df['Opened_dt']= df['Opened_dt'].astype('str')
    if 'Closed_dt' in df.columns:
        df['Closed_dt']= df['Closed_dt'].astype('str')

    # then save
    df.to_csv(path_or_buf=newfilename)
    return newfilename

def process_timedelta(df):
    """Takes a DateFrame with datetimes already coonverted for times
    RETURNS a pandas DataFrame with timedeltas for case total open time."""

    df['Case_Time'] = df['Closed_dt']-df['Opened_dt']
    df['Case_Sec'] = delta2sec(df['Case_Time'])

    return df

# change name to process_datetimes and remove CaseTime and Case_Sec
def process_datetime(df):     
    """Loads a raw dataset, reformats some rows for faster processing and saves 
    to a new file for efficiently reading in later with load_data().
    Creates the 'Opened_dt' and 'Closed_dt' columns.
    Move save functionality to another function."""

    # generate new columns with datetime format for efficient calculations
    # and total case time open in seconds
    if 'Opened_dt' in df.columns:
        df['Opened_dt']= pd.to_datetime(df['Opened_dt'])
    else:
        print 'Datetime efficient string not found. Processing: wait 10 min.'
        df['Opened_dt']= pd.to_datetime(df['Opened'])
    sys.stdout.flush()    # display progress if %time
    if 'Closed_dt' in df.columns:
        df['Closed_dt']= pd.to_datetime(df['Closed_dt'])
    else:
        print 'Datetime efficient string not found. Processing: wait 10 min.'
        df['Closed_dt']= pd.to_datetime(df['Closed'])
    return df


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
#   return dist_mean[sup_dist]
    return opendate + dist_mean[sup_dist]

#    return sec2delta(duration)
#    return model_mean


