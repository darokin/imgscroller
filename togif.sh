
#!/bin/bash

#Images to mp4 with aspect ratio constrain
#ffmpeg -f image2 -i "$1"_%04d.png -vf "scale=1080:1080:force_original_aspect_ratio=1,pad=1080:1080:(ow-iw)/2:(oh-ih)/2:color=black" -c:v libx264 -pix_fmt yuv420p "$1"_tmp.mp4

# Images to mp4
#./ffmpeg -f image2 -i "$1"_%04d.png -c:v libx264 -pix_fmt yuv420p "$1".mp4
c:/Apps/ffmpeg -f image2 -i "$1"_%04d.png -c:v libx264 -pix_fmt yuv420p "$1".mp4

# Make a GIF
#./ffmpeg -i "$1".mp4 -pix_fmt rgb24 -loop 0 "$1".gif

# Make 4x repeat mp4
#for i in {1..4}; do printf "file '%s'\n"  "$1".mp4 >> list.txt; done
#./ffmpeg -f concat -i list.txt -c copy "$1"_x4.mp4
#rm list.txt

# Convert
#./ffmpeg -i "$1".mp4 -c:v libx264rgb -pix_fmt yuv420p "$1"_rgb.mp4
#c:/Apps/ffmpeg -i "$1".mp4 -c:v libx264rgb -pix_fmt yuv420p "$1"_rgb.mp4