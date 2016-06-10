#!/usr/bin/env python

import sys
import json

if len(sys.argv) < 3:
    print "You have to pass the path to the slides.json and a output path!"
    sys.exit(1)

slide_filepath = sys.argv[1]
ffconcat_filepath = sys.argv[2]

with open(slide_filepath, 'r') as slides_file:
    slides = json.load(slides_file)

slides[0]["slide"]["begin"] = 0

out = 'ffconcat version 1.0\n';
for slide in slides:
    img_path = slide["slide"]["local"]
    begin = int(slide["slide"]["begin"])
    end = int(slide["slide"]["end"])
    # duration in seconds
    duration = round((end - begin) / float(1000), 2)
    out += "file {}\nduration {}\n".format(img_path, duration)

with open(ffconcat_filepath, 'w') as ffconcat_file:
    ffconcat_file.write(out)
