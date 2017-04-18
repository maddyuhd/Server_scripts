import cv2
# import time as t
# import numpy as np
import sys

def imresize(img, new_val=320):

    h, w = img.shape[:2]

    ar = w / float(h)

    if h > w:
        ar = w / float(h)
        newH = new_val
        newW = int(newH * ar)

    elif h < w:
        ar = h / float(w)
        newW = new_val
        newH = int(newW * ar)

    else:
        newH = new_val
        newW = new_val

    img = cv2.resize(img, (newW, newH))

    return img, newH, newW


def count_frames_manual(video_path):

    video = cv2.VideoCapture(video_path)

    total = 0

    while True:

        (grabbed, frame) = video.read()

        if not grabbed:
            break

        total += 1

    return total


def count_frames(video_path, override=False):

    video = cv2.VideoCapture(video_path)

    total = 0

    if override:
        total = count_frames_manual(video)
        # otherwise, let's try the fast way first
    else:
        try:
            total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        except:
            total = count_frames_manual(video_path)

    # print ("Total frames :", total)

    points = total * .01

    video.set(1, points)

    ret, frame = video.read()

    image_res, h, w = imresize(frame, thumnail_size)

    cv2.imwrite(str(thumnail_name) + ".jpg", image_res)
    
    video.release()


# start = t.time()

# video_path = "/home/smacar/Downloads/test.mp4"
video_path = sys.argv[1]
s = video_path.rfind('/')

thumnail_name = video_path[s + 1:-4]

thumnail_size = 200

num = count_frames(video_path)

# end = t.time()

# print("Time Taken: ", str((end - start)))
