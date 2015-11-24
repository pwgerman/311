# python 2.7

import pdb

import urllib2
import shutil
import urlparse
import os
import datetime

def download_csv(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv', savefilename):
    """Downsloads csv file of 311 case data from SF server.  Arguments are
    URL of file and path/filename for locally saving the file."""
    urllib.urlretrieve(url, "urllib_test.csv")


# https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
def download_url(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv', as_filename=None):
    # url = "https://i.imgur.com/G0IKECz.jpg"
    # url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv'

    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    pdb.set_trace()
    # meta.headers   # will list headers available
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

# download_url()
# download_url(url="https://i.imgur.com/G0IKECz.jpg")


# https://stackoverflow.com/questions/862173/how-to-download-a-file-using-python-in-a-smarter-way
def append2filename(filename, add=None):
    """Appends extra string to end of filename, before the first 'dot' extension.
    If no second arguement given, the current date is appended."""
    if add==None:
        add = datetime.datetime.now().strftime('%Y-%m-%d')
    basename = filename.split('.')[0]
    extname = filename.split('.')[1:]
    fullname = basename + add + '.' + ''.join(extname)
    print fullname
    return fullname

def download(url, fileName=None):
    def getFileName(url,openUrl):
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            cd = dict(map(
                lambda x: x.strip().split('=') if '=' in x else (x.strip(),''),
                openUrl.info()['Content-Disposition'].split(';')))
            pdb.set_trace()  # (Pdb) p openUrl.info().headers
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
        pdb.set_trace() # (Pdb) p fileName
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)  # automatically buffers downloads of very large files
    finally:
        r.close()

download(url = "https://i.imgur.com/G0IKECz.jpg")
# download(url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv')
    # url = "https://i.imgur.com/G0IKECz.jpg"
    # url='https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv'

# append2filename(filename='This_is_a_name.csv')

# import datetime
    # datetime.datetime.now().strftime('%Y-%m-%d')  # add to filename string


# mod = r.info().getheader('Last-Modified')
# 'Mon, 23 Nov 2015 10:02:55 PST'
# datetime.datetime.strptime(mod, '%a, %d %b %Y %X %Z')

# # check if file already exists before downloading again
# import os.path
# os.path.isfile(fname) 

