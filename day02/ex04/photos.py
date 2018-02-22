#!/usr/bin/env python3

import urllib
import urllib.request
import re
import os
import sys
from os.path import basename
from urllib.parse import urlparse
from posixpath import basename,dirname
 
if len(sys.argv) > 1:
    if not sys.argv[1].startswith("http"):
        print("Error please use a proper url with http or https")
        sys.exit()
    url=urlparse(sys.argv[1])
    dirname=basename(url.netloc)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    os.chdir(dirname)
    urlcontent=urllib.request.urlopen(sys.argv[1]).read()
    imgurls=re.findall('img .*?src="(.*?)"',str(urlcontent))
    for imgurl in imgurls:
        try:
            urllib.request.urlretrieve(url.scheme + "://" + url.netloc + imgurl, basename(imgurl))
        except:
            pass
        try:
            urllib.request.urlretrieve(imgurl, basename(imgurl))
        except:
            pass
