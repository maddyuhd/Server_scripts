import sys
import os

videoPath = sys.argv[1]
videoOutput = sys.argv[2]

videoOutput = videoOutput+".mp4"

os.system("ffmpeg -i "+videoPath+" -strict -2 -c:v libx264 "+videoOutput)



