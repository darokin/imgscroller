
#!/bin/bash

echo "file $1"
fname=${1%????}
echo "fname $fname"

# Launch img scroller
python imgscroller.py "$@"

# Images to mp4
c:/Apps/ffmpeg -f image2 -i "$fname"_%04d.png -c:v libx264 -pix_fmt yuv420p "$fname".mp4

rm "$fname"_*.png