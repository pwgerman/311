# python 2.7

def download_csv(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv', savefilename):
    """Downsloads csv file of 311 case data from SF server.  Arguments are
    URL of file and path/filename for locally saving the file."""
    urllib.urlretrieve(url, "urllib_test.csv")

