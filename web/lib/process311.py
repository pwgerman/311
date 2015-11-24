# python 2.7

import ml311

rawdata_filename = '/Users/walter/Data/SF/Case_Data_from_San_Francisco_311__SF311_2015-10-22.csv'
# procdata_filename = rawdata_filename.strip('.cvs')+'proc.csv'

def make_proc_filename(rawdata_filename):
    """Returns the filename for processed datafile."""
    procdata_filename = rawdata_filename.strip('.cvs')+'proc.csv'
    return procdata_filename


if __name__ == "__main__":
	procdata_filename = make_proc_filename(rawdata_filename)