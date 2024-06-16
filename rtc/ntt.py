import os
import easyocr
import numpy as np
import cv2

def text_rec(path):
    img = cv2.imread(path)
    img = inlargeimg(cv2.imread(path))
    reader=easyocr.Reader(["en"],
                          recog_network='custom_example',
                          )
    res = reader.readtext(img,allowlist="0123456789ABEKMHOPCTYX",paragraph=True,detail=0)
    delelepath(path)

    return res[0].split(' ')[0]

def inlargeimg(image):
    # width = 213
    # # height = 67
    # din = (image.shape[1]*2, image.shape[0]*2)
    # resized = cv2.resize(image, din,interpolation=cv2.INTER_AREA)
    # image resizing
    img = cv2.resize(
        image,None,fx=2,fy=2,
        interpolation=cv2.INTER_AREA)

    # converting image to grayscale
    img = cv2.cvtColor(
        img, cv2.COLOR_BGR2GRAY)

    img = cv2.dilate(img, kernel=np.ones((2, 2)), iterations=1)
    # denoising the image
    # img = cv2.GaussianBlur(
    #     img, (5, 5), 0)

    return img

def delelepath(path):
    os.remove(path)
    os.rmdir('C:\\Users\Шнырь\Desktop\диплом\\backend\\runs\detect\predict\crops\\num')
    os.rmdir('C:\\Users\Шнырь\Desktop\диплом\\backend\\runs\detect\predict\crops')
    os.rmdir('C:\\Users\Шнырь\Desktop\диплом\\backend\\runs\detect\predict')