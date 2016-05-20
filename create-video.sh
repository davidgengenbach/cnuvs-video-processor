#!/usr/bin/env sh

ERR=0
if [ ! -d data ]; then
  echo "Needed directory 'data' does NOT exist" && ERR=1
fi

if [ ! -f data/slides.json ]; then
  echo "Needed file 'data/slides.json' does NOT exist" && ERR=1
fi

if [ ! -f data/video.mp4 ]; then
  echo "Needed file 'data/video.mp4' does NOT exist" && ERR=1
fi

if [ $ERR == 1 ]; then
    exit 1
fi

set -x

# Extract audio from video and copy left channel to right
ffmpeg -i data/video.mp4 -q:a 0 -map a -vcodec copy -ab 220k -ar 48000 -ac 1 data/audio.ogg

# Create slide file to create video with slides
./create-ffconcat-file.py

# Create video from slides and audio
ffmpeg -i data/in.ffconcat -i data/audio.ogg -vf fps=4 data/out.mp4

echo "Your video is now in data/out.mp4"