#!/usr/bin/env python

import json

slides_file = open('data/slides.json', 'r')
slides = json.load(slides_file)

out = 'ffconcat version 1.0\n';
for slide in slides:
    img_path = slide["slide"]["local"]
    begin = slide["slide"]["begin"]
    end = slide["slide"]["end"]
    # duration in seconds
    duration = (end - begin) / 1000
    out += "file {}\nduration {}\n".format(img_path, duration)

ffconcat_file = open('data/in.ffconcat', 'w')
ffconcat_file.write(out)
