import numpy as np
import file
import imgutil
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--imagepath", required=True,
                help="Folder path to image")

ap.add_argument("-m", "--watermark", required=True,
                help="Path to watermark image")

args = vars(ap.parse_args())

image_path = args["imagepath"]
water_path = args["watermark"]

images = file.readfolder(image_path)

if images is not None:

    for imgs in images:
        img = imgutil.imread(image_path + imgs)
        h, w = imgutil.imd(img)

        water_img = imgutil.imread(water_path)
        new_h, new_w = imgutil.imd(water_img)

        if new_w >= w:
            watermark_resized = imgutil.imresize(water_img, new_w, new_h, w)
            new_rh, new_rw = imgutil.imd(watermark_resized)

        else:
            print("error: invalid water marker")

        mask = np.zeros((h + new_rh, w, 3), np.uint8)
        mask[0:h, 0:w] = img[0:h, 0:w]
        mask[h:h + new_rh, 0:w] = watermark_resized[0:new_rh, 0:new_rw]

        imgutil.imwrite(imgs + "_mark.jpg", mask)

else:
    print ("error: empty folder")
