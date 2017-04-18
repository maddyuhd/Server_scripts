import argparse
import cv2
import imgutil

ap = argparse.ArgumentParser()

ap.add_argument("-v", "--videopath", required=True,
                help="Path to input Video")
ap.add_argument("-s", "--size", required=True,
                help="Thumbnail size of the output Image")

args = vars(ap.parse_args())


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

    h, w = imgutil.imd(frame)

    image_res = imgutil.imresize(frame, w, h, int(args["size"]))

    cv2.imwrite(str(thumnail_name) + ".jpg", image_res)

    video.release()


s = args["videopath"].rfind('/')

thumnail_name = args["videopath"][s + 1:-4]

num = count_frames(args["videopath"])
