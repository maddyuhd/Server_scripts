import argparse
import os


ap = argparse.ArgumentParser()

ap.add_argument("-v", "--videopath", required=True,
                help="Path to input Video")
ap.add_argument("-o", "--outname", required=True,
                help="Name of the output Video")

args = vars(ap.parse_args())

os.system("ffmpeg -i "+args["videopath"]+" -strict -2 -c:v libx264 "+args["outname"]+".mp4")
