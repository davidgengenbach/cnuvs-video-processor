#!/usr/bin/env python


import urllib
import os
import sys
import json

if len(sys.argv) < 3:
    print "Usage: {} folder URL".format(sys.argv[0])
    sys.exit(1)

output_path = sys.argv[1]
url = sys.argv[2]

ID = url.split('/')[-1]
ID_SPLITTED = '/'.join(ID.split('-'))

SLIDES_URL = "http://clls.rbg.informatik.tu-darmstadt.de:8080/api/slides/{}".format(ID)
VIDEO_URL = "http://clls.rbg.informatik.tu-darmstadt.de/clls/lecturematerial/{}/videos/video.mp4".format(ID_SPLITTED)

# Create output path
try:
    os.mkdir(output_path)
except OSError:
    pass

def download_progress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      sys.stdout.write("\r-> %d%%" % percent)
      sys.stdout.flush()

def download_if_not_existent(url, path):
    if not os.path.isfile(path):
        print "Downloading file: {}".format(path)
        urllib.urlretrieve(url, path, reporthook=download_progress)
        print "=> Finished"
    else:
        print "File already downloaded: {}".format(path)

print "Downloading slides"
download_if_not_existent(SLIDES_URL, "{}/slides.json".format(output_path))

print "Downloading video (this may take a while)"
download_if_not_existent(VIDEO_URL, "{}/video.mp4".format(output_path))