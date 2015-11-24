# python 2.7

import pdb

import urllib2

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

download_url()
# download_url(url="https://i.imgur.com/G0IKECz.jpg")
