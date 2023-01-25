import sys
import os
import glob
from math import floor, ceil
import random
from PIL import Image, ImageOps, ImageDraw
import argparse

VERSION_NUM = "0.0.1"
nfoData = r"""
             ___________________
  ┌─────____/   \___   \        \─────────────┐
  │    /   /    /   \   \    \__/ - darokin - │
  │----\_______/\_______/\___/----------------│
  │                                           │
  │ imgscroller v0.0.1                   2023 │
  │ Image to scrolling vertical video         │
  │                                           │
  │ https://github.com/darokin/imgscroller    │
  └───────────────────────────────────────────┘
"""

frameCount = 0

def imgscroller(path, img, destHeight, speed, pause):
	
	global frameCount

	if not img:
		print("Impossible de lire l'image\n")
		return

	# Step and pause 
	step = speed
	nbFramePause = int(25 * pause)

	img = img.convert("RGBA")
	print(img.format, img.size, img.mode)
	
	# storing the sizes
	width, height = img.size

	sys.stdout.write(f"Generating video from image '{path}' size : [{width},{height}]\n")

	# Filename for destination images 
	#filenameStart = path.split("/")
	#filenameStart = filenameStart[len(filenameStart) - 1].split(".")
	filenameStart = path.split(".")[0]

	# PAUSE UP START
	for pauseCount in range(0, nbFramePause // 2):
		outputFrame(img.crop((0, 0, width, destHeight)), width, destHeight, filenameStart)

	# SCROLL DOWN
	# create destination images for scroll down
	for decalUp in range(0, (height - destHeight), step):
		#imgDest = Image.new("RGBA", [width, destHeight])
		regionUp	 = 0 + decalUp
		reg = img.crop((0, regionUp, width, regionUp + destHeight))
		outputFrame(reg, width, destHeight, filenameStart)

	# PAUSE DOWN
	for pauseCount in range(0, nbFramePause):
		regionUp	 = 0 + (height - destHeight)
		reg = img.crop((0, regionUp, width, regionUp + destHeight))
		outputFrame(reg, width, destHeight, filenameStart)

	# SCROLL UP
	# create destination images for scroll up
	for decalDown in range((height - destHeight), 0, -step):
		#imgDest = Image.new("RGBA", [width, destHeight])
		regionUp	 = 0 + decalDown
		reg = img.crop((0, regionUp, width, decalDown + destHeight))
		outputFrame(reg, width, destHeight, filenameStart)

	# PAUSE UP END
	for pauseCount in range(0, nbFramePause // 2):
		outputFrame(img.crop((0, 0, width, destHeight)), width, destHeight, filenameStart)
	
	sys.stdout.write(f"END\n")

def outputFrame(img, w, h, fnames):
	global frameCount

	imgDest = Image.new("RGBA", [w, h])
	imgDest.paste(img, (0, 0))
	# sys.stdout.write(f"Output frame '{frameCount}'\n")
	frameCount += 1 
	imgDest.convert("RGB").save("" + fnames + "_" + "{:0>4d}".format(frameCount) + ".png")

def init():
	# ================================================================
	# START

	# Argument parsing
	parser = argparse.ArgumentParser(description="IMGDECO decorate images", add_help=False)
	parser._positionals.title = 'Positional arguments'
	parser.add_argument("img", help="Path to the image(s) to convert", type=str)
	parser._optionals.title = 'Optional arguments'
	parser.add_argument("-h", "--height", type=int, default=1920, help="output height")
	parser.add_argument("-s", "--speed", type=int, default=10, help="speed (1 = slow ; 30 = fast (default = 10))")
	parser.add_argument("-p", "--pause", type=float, default=1.8, help="pause (nb seconds (float) pause start, bottom, end)")

	args = parser.parse_args()

	# args.img = "output/c1_0001.png"

	# File Handling
	fileList = glob.glob(args.img)
	for infile in fileList:
		try:
			print(f"Processing file {infile}")
			with Image.open(infile) as im:
				imgscroller(infile, im, args.height, args.speed, args.pause)
		except OSError:
			print("error")
			sys.stdout.write(f"ERROR Can't load image file {infile}\n")
			pass

init()
