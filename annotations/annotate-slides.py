#!/usr/bin/env python
# pylint: disable-msg=C0103

import json
import re
from PIL import Image, ImageDraw

f_commands = open("commands.json", "r")
f_slides = open("slides.json", "r")

commands = json.load(f_commands)
slides = json.load(f_slides)

slides = sorted(slides, key=lambda slide: int(slide["slide"]["begin"]))
commands = sorted(commands, key=lambda command: int(command["start"]))

def get_slide_for_time( time ):
    for slide in slides:
        if int(slide["slide"]["end"]) > time and int(slide["slide"]["begin"]) < time:
            return slide
    raise Exception("No Slide found for time: {}".format(time))

def get_image_from_slide( slide ):
    return 'images/' + slide["slide"]["img"].split("/")[-1]

slides[0]["slide"]["begin"] = "0"

current_slide = None
current_slide_img = None
im = None
draw = None
current_position = (0, 0)
stroke_color = (0, 0, 0)
dim_image = (0, 0)
dim_command = (0, 0)
counter = 0
ratio_w = 0
ratio_h = 0
line_width = 1
counter = 0
changed = 0
original_image = None
new_slides = []

def save_image(command_start, command_end):
    global changed
    global counter
    global new_slides
    if changed == 0:
        return
    filepath = 'images/_COUNTER_' + str(counter) + '.png'
    im.save(filepath)
    im.close()
    changed = 0
    counter = counter + 1
    start_time = command_start["start"]
    end_time = command_end["start"]
    new_slides.append({
        "slide": {
            "begin": start_time,
            "end": end_time,
            "local": filepath
        }
    })


start_command = None
for command in commands:
    start_time = int(command["start"])
    if current_slide is None or start_time > int(current_slide["slide"]["end"]):
        if not im is None:
            save_image(start_command, command)
        start_command = command
        current_slide = get_slide_for_time(start_time)
        im = Image.open(get_image_from_slide(current_slide))
        original_image = im.copy()
        draw = ImageDraw.Draw(im)
        dim_image = im.size
        counter = counter + 1

    for l_command in command["commands"]:
        if "moveTo" in l_command:
            m = re.search('moveTo\((.*?),(.*?)\)', l_command)
            x = int(m.group(1)) * ratio_w
            y = int(m.group(2)) * ratio_h
            current_position = (x, y)
        elif "lineTo" in l_command:
            m = re.search('lineTo\((.*?),(.*?)\)', l_command)
            x = int(m.group(1)) * ratio_w
            y = int(m.group(2)) * ratio_h
            draw.line([current_position, (x, y)], fill=stroke_color, width=line_width * 3)
            changed = 1
            # Draw line to
        elif "clear" in l_command:
            save_image(start_command, command)
            start_command = command
            im = original_image.copy()
            draw = ImageDraw.Draw(im)
        elif "width" in l_command:
            width = int(l_command.split("=")[1].split(",")[0])
            height = int(l_command.split("=")[-1])
            dim_command = (width, height)
            ratio_w = (dim_image[0] / float(dim_command[0]))
            ratio_h = (dim_image[1] / float(dim_command[1]))
        elif "strokeStyle" in l_command:
            m = re.search('strokeStyle=\'rgba\((.*?),(.*?),(.*?),(.*?)\)\'', l_command)
            stroke_color = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        elif "lineWidth" in l_command:
            pass
            #line_width = int(l_command.split("=")[-1])
        else:
            print "command unknown: {}".format(l_command)


with open('slides-new.json', 'w') as outfile:
    json.dump(new_slides, outfile)
