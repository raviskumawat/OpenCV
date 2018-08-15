import cv2
import numpy as np
import random
img=cv2.imread('fuzzy.png',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray",gray)

blur=cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("Blur",blur)

thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,205,1)
cv2.imshow("thresh",thresh)
kernel = np.ones((5,5), np.uint8)*255
img_dilate=cv2.dilate(thresh,kernel,iterations=1)
#cv2.imshow("img_dilate",img_dilate)

img_erode=cv2.erode(img_dilate,kernel,iterations=5)
cv2.imshow("img_erode",img_erode)

_,contors,hierarchy=cv2.findContours(img_erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

filtered=[]

for c in contors:
    if cv2.contourArea(c)>1000:filtered.append(c)

empty=np.zeros((img.shape[0],img.shape[1]),'uint8')
for c in filtered:
    color=(random.randint(100,255),random.randint(0,255),random.randint(0,255))
    cv2.drawContours(empty,[c],-1,color,-1)

cv2.imshow("img_final",empty)







'''
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
img_split=np.concatenate((h,s,v),axis=1)
#cv2.imshow("Split",img_split)
img1=cv2.medianBlur(img,13)
#cv2.imshow("Blur",img1)
kernel = np.ones((3,3), np.uint8)*255
img_erode=cv2.erode(img,kernel,iterations=2)
#cv2.imshow("img_erode",img_erode)
img_dilate=cv2.dilate(img_erode,kernel,iterations=2)
#cv2.imshow("img_dilate",img_dilate)
img_morph=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_dilate1=cv2.cvtColor(img_dilate,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(img1,220,190)

img_erode=cv2.dilate(edges,kernel,iterations=3)
cv2.imshow("edges",img_erode)
print(edges)

_,contors,hierarchy=cv2.findContours(img_erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2=img.copy()
index=-1
color=(255,0,255)
cv2.drawContours(img,contors,index,color,4)
#cany=cv2.Canny(img_dilate,)
cv2.imshow("img_final",img)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()