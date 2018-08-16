import urllib.request
import  urllib
import cv2
import numpy as np
#from matplotlib import *
#from skimage import io
url='http://10.5.46.17:8080/photo.jpg' #my webcam is not working ,so i am using mobile camera
imgr=urllib.request.urlopen(url)
imgnp=np.array(bytearray(imgr.read()),dtype=np.uint8)
im=0
while True:
    imgr=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imgr.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    cv2.imshow('video',img)
    im=im+1
    if ord('q')==cv2.waitKey(10):
        break

gray_image = cv2.cvtColor(imgnp, cv2.COLOR_BGR2GRAY)
hsvimg=colors.rgb_to_hsv(imgnp)

cv2.imshow(grayimg)
cv2.imshow(hsvimg)
