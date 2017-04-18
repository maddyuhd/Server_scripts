import cv2
import argparse
import imgutil


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,
                help="path to input image")

ap.add_argument("-s", "--size", required=True,
                help="size of the output image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

h, w = imgutil.imd(img)

re_img = imgutil.imresize(img, w, h, int(args["size"]))

s = args["image"].rfind('/')

output_name = args["image"][s + 1:-4]

cv2.imwrite(output_name + 'resized.jpg', re_img)
