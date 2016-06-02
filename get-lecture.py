#!/usr/bin/env python


import urllib
import os
import sys
import json

if len(sys.argv) < 3:
    print "You have to pass the url to the lecture and an output folder!"
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

def download_if_not_existent(url, path):
    if not os.path.isfile(path):
        print "Downloading file: {}".format(path)
        urllib.urlretrieve(url, path)
        print "=> Finished"
    else:
        print "File already downloaded: {}".format(path)


print "Downloading slides"
download_if_not_existent(SLIDES_URL, output_path + '/' + 'slides.json')

print "Downloading video (this may take a while)"
download_if_not_existent(VIDEO_URL, output_path + '/' + 'video.mp4')