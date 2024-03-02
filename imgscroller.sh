#!/bin/bash

#echo "file $1"
# Remove extension (4 ending characters)
fname=${1%????}
#echo "fname $fname"

# Launch img scroller that generates all the images of the video
python3 imgscroller.py "$@"

echo "Generating "$fname".mp4 video with ffmpeg"

# Images to mp4
ffmpeg -f image2 -i "$fname"_%04d.png -c:v libx264 -pix_fmt yuv420p "$fname".mp4

# Remove images used to make the video
rm "$fname"_*.png

