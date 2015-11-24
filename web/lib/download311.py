# python 2.7

import pdb

import urllib2
import shutil
import urlparse
import os
import datetime

def download_csv(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv', savefilename="urllib_test.csv"):
    """Downsloads csv file of 311 case data from SF server.  Arguments are
    URL of file and path/filename for locally saving the file."""
    urllib.urlretrieve(url, savefilename)

# https://stackoverflow.com/questions/862173/how-to-download-a-file-using-python-in-a-smarter-way
def append2filename(filename, add=None):
    """Appends extra string to end of filename, before the first 'dot' extension.
    If no second arguement given, the current date is appended."""
    if add==None:
        add = datetime.datetime.now().strftime('%Y-%m-%d')
    basename = filename.split('.')[0]
    extname = filename.split('.')[1:]
    fullname = basename + add + '.' + ''.join(extname)
    return fullname

def download(url, fileName=None):
    """Downloads URL to local destination filename."""
    def getFileName(url,openUrl):
        """Returns filename based on URL response headers."""
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            cd = dict(map(
                lambda x: x.strip().split('=') if '=' in x else (x.strip(),''),
                openUrl.info()['Content-Disposition'].split(';')))
            if 'filename' in cd:
                filename = cd['filename'].strip("\"'")
                if filename:   #return filename
                    if 'Last-Modified' in openUrl.info(): 
                        mod = openUrl.info()['Last-Modified']
                        mod_dt = datetime.datetime.strptime(mod, '%a, %d %b %Y %X %Z')
                        mod_name = datetime.datetime.strftime(mod_dt, '%Y%m%d-%H%M')
                        filename = append2filename(filename, add=mod_name)
                    else:
                        print "'Last-Modified' datetime not in URL header."
                        print "Todays date added to filename."
                        filename = append2filename(filename)
                    return filename
        # if no filename was found above, parse it out of the final URL.
        filename = os.path.basename(urlparse.urlsplit(openUrl.url)[2])
        print "'Content-Disposition' not in URL header."
        print "Today's date added to URL for filename."
        return append2filename(filename)

    r = urllib2.urlopen(urllib2.Request(url))
    pdb.set_trace()  # (Pdb) p r.info().headers
    try:
        fileName = fileName or getFileName(url,r)
        print fileName
        # if fileName already exists:
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)  # automatically buffers downloads of very large files
        # else print "File by that name already exists."
    finally:
        r.close()


if __name__ == "__main__":

    # url = "https://i.imgur.com/G0IKECz.jpg"
    url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv'
    download(url=url)
    # download(url = "https://i.imgur.com/G0IKECz.jpg")
    # download(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv')


# TO DO

# # check if file already exists before downloading again
# import os.path
# os.path.isfile(fname) 

# Create menu for 'main' that lets choose to see if up to date or download 311 or something custom.


