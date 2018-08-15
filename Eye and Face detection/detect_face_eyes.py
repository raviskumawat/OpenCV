import cv2
import numpy as np

img=cv2.imread('faces.jpeg',1)

path_faces='haarcascade_frontalface_default.xml'
path_eyes='haarcascade_eye.xml'

face_cascade=cv2.CascadeClassifier(path_faces)

eye_cascade=cv2.CascadeClassifier(path_eyes)

faces=face_cascade.detectMultiScale(img)

eyes=eye_cascade.detectMultiScale(img)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

for (x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)

cv2.imshow("Detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
