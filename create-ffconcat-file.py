#!/usr/bin/env python

import sys
import json

if len(sys.argv) < 3:
    print "You have to pass the path to the slides.json and a output path!"
    sys.exit(1)

slide_filepath = sys.argv[1]
ffconcat_filepath = sys.argv[2]

slides_file = open(slide_filepath, 'r')
slides = json.load(slides_file)

slides[0]["slide"]["begin"] = 0

out = 'ffconcat version 1.0\n';
for slide in slides:
    img_path = slide["slide"]["local"]
    begin = int(slide["slide"]["begin"])
    end = int(slide["slide"]["end"])
    # duration in seconds
    duration = (end - begin) / 1000
    out += "file {}\nduration {}\n".format(img_path, duration)

ffconcat_file = open(ffconcat_filepath, 'w')
ffconcat_file.write(out)
