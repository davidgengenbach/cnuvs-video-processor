#!/usr/bin/env python
# pylint: disable-msg=C0103

import json
import re
from PIL import Image, ImageDraw

f_slides = open("slides.json", "r")
slides = json.load(f_slides)
slides = sorted(slides, key=lambda slide: slide["slide"]["begin"])

f_slides_new = open("slides-new.json", "r")
slides_new = json.load(f_slides_new)
slides_new = sorted(slides_new, key=lambda slide: slide["slide"]["begin"])

slides[0]["slide"]["begin"] = "0"


def merge_slides(slidesA, slidesB):
    for slide_b in slidesB:
        begin_b = int(slide_b["slide"]["begin"])
        end_b = int(slide_b["slide"]["end"])
        for slide_a in slidesA:
            begin_a = int(slide_a["slide"]["begin"])
            end_a = int(slide_a["slide"]["end"])
            if begin_b >= begin_a and end_b <= end_a:
                slidesA.insert(slidesA.index(slide_a) + 1, slide_b)
                break
    return slidesA

out = sorted(merge_slides(slides, slides_new), key=lambda slide: int(slide["slide"]["begin"]))


with open('slides-merged.json', 'w') as outfile:
    json.dump(out, outfile)
