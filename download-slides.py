#!/usr/bin/env python


import urllib
import os
import sys
import json

if len(sys.argv) < 3:
    print "You have to pass the path to the slides.json and a output path!"
    sys.exit(1)

filepath = sys.argv[1]
output_filepath = sys.argv[2]

with open(filepath, 'r') as slides_file:
    slides = json.load(slides_file)

try:
    os.mkdir(output_filepath + '/images')
except OSError:
    # Ignore this
    print "Image folder already existing"

for slide in slides:
    if slide["slide"]["img"] is None:
        continue
    img_path = slide["slide"]["img"]
    img_local_path = "images/" + img_path.split("/")[-1]
    img_local_realpath = output_filepath + '/' + img_local_path
    if not os.path.isfile(img_local_realpath):
        print "Downloading file: {}".format(img_local_path)
        urllib.urlretrieve(img_path, img_local_realpath)
    else:
        print "File already downloaded: {}".format(img_local_path)
    slide["slide"]["local"] = img_local_path

with open(filepath, 'w') as slides_file:
    json.dump(slides, slides_file)
