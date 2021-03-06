#!/usr/bin/env sh

FOLDER=$1
VIDEO_FILE=$FOLDER/video.mp4
VIDEO_OUT_FILE=$FOLDER/out.mp4
SLIDES_FILE=$FOLDER/slides.json
FFCONCAT_FILE=$FOLDER/in.ffconcat

echo "Starting conversion in folder: '$1'"

ERR=0
if [ ! -d $FOLDER ]; then
  echo "Needed directory '$FOLDER' does NOT exist" && ERR=1
fi

if [ ! -f $VIDEO_FILE ]; then
  echo "Needed file '$VIDEO_FILE' does NOT exist" && ERR=1
fi

if [ ! -f $SLIDES_FILE ]; then
  echo "Needed file '$SLIDES_FILE' does NOT exist" && ERR=1
fi

if [ $ERR == 1 ]; then
    exit 1
fi

set -x


# Download slide files
./download-slides.py $SLIDES_FILE $FOLDER || exit 1

# Create slide file to create video with slides
./create-ffconcat-file.py $SLIDES_FILE $FFCONCAT_FILE || exit 1

# Extract audio from video and copy left channel to right
ffmpeg -i $VIDEO_FILE -q:a 0 -map a -vcodec copy -ac 1 $FOLDER/audio.mp4 || exit 1

# Create video from slides and audio
ffmpeg -i $FFCONCAT_FILE -i $FOLDER/audio.mp4 -c:a copy -vf fps=5 $VIDEO_OUT_FILE || exit 1

echo "Your video is now in '$VIDEO_OUT_FILE'"

#ffmpeg -i 1_a.mp4 -filter:a "atempo=2.0" -vn 1_a_speedup.mp4
#ffmpeg -i video.mp4 -q:a 0 -map a -vcodec copy -ac 1 audio.mp4
#ffmpeg -i video.mp4 -vn -c:a copy audio.mp4
#ffmpeg -i in.ffconcat -i audio.mp4 -c:a copy -vf fps=5 out.mp4