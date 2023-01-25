# imgscroller

![Python application](https://github.com/darokin/darshell-clock/workflows/Python%20application/badge.svg)

**imgscroller** allows you to convert images to vertical scrolling MP4.
My usage of it is using a vertical picture of an ASCII art ♥ export to make a scrolling video showing all the picture from top to bottom.

## Usage

 > ./imgscroller.sh data/picture.png

The bash script launch the python script that generate pictures (which are deleted afterwards) then it passes the images to FFMPEG so you end up with a video named :
 * data/picture.mp4

The program can take these arguments
```
 img             Path to the image
-h --height      Destination height of the video
-s --step        Number of pixel jumps between each frame (default = 10)
-p --pause       Number of seconds (float) for the bottom pause (default = 1.8)
                 Half of that pause is also made at the start and at the end of the animation
```

So you can do this to have a quick (depending on your image height) boomerang video with no pausing :
 > ./imgscroller.sh data/picture.png -s 30 -p 0

Or this to have a super slow scrolling and a 4 second pause :
 > ./imgscroller.sh data/picture.png -s 2 -p 4
