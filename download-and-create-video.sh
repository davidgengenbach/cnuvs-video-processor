#!/usr/bin/env sh

OUTPUT_FOLDER=$1
LECTURE_URL=$2

set +x

if [ -z $OUTPUT_FOLDER ] || [ -z $LECTURE_URL ]; then
  echo "Usage: $0 OUTPUT_FOLDER LECTURE_URL" && exit 1
fi

./get-lecture.py $OUTPUT_FOLDER $LECTURE_URL || exit 1
./create-video.sh $OUTPUT_FOLDER || exit 1