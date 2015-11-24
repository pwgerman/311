# python 2.7
"""Process SF 311 Datafiles.
make_proc_filename  Creates new filename for processed datafile
load_new_data  Begins processing a newly downloaded datafile
load_proc_data  Faster loading of datafiles that have already received
initial processing.
Additional argument from shell command line initiates script with rawdata_filename
$ python process311.py <rawdata_filename>"""

import ml311
import sys

def make_proc_filename(rawdata_filename):
    """Returns the filename for processed datafile."""
    procdata_filename = rawdata_filename.strip('.cvs')+'proc.csv'
    return procdata_filename

def load_new_data(rawdata_filename, procdata_filename):
    """Takes a raw SF 311 csv datafile, processes the dates into datetime
    format and then saves the output for faster loading in the future.
    Also, returns the processed pandas DataFrame."""
    print 'This may take a few minutes to load'
    t0 = time.time()
    df = ml311.load_data(rawdata_filename)
    print str(time.time()-t0) + ' seconds elapsed'
    sys.stdout.flush()    # print before executing next statement
    t0 = time.time()
    df = ml311.process_datetime(df)
    ml311.save_data(df, procdata_filename)
    print str(time.time()-t0) + ' seconds elapsed'
    return df

def load_proc_data(procdata_filename):
    """Opens a processed SF 311 datafile (previously opened with load_new_data)
    and returns the pandas DataFrame."""
    print 'This may take a few minutes to load'
    t0 = time.time()
    df = ml311.load_data(procdata_filename)
    print str(time.time()-t0) + ' seconds elapsed'
    t0 = time.time()
    df = ml311.process_timedelta(df)
    print str(time.time()-t0) + ' seconds elapsed'
    return df

if __name__ == "__main__":
	rawdata_filename = '/Users/walter/Data/SF/Case_Data_from_San_Francisco_311__SF311_2015-10-22.csv'
	procdata_filename = make_proc_filename(rawdata_filename)

