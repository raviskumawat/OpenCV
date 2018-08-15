import cv2
import numpy as np
canvas=np.ones((500,500,3),'uint8')*255
cv2.namedWindow('canvas')
global_x=0
global_y=0
color=(0,0,0)
def enable_draw(event,x,y,flags,param):
    global global_x
    global global_y
    if event==cv2.EVENT_LBUTTONDOWN:
        print("MOUSE CLICKED:x=",x," y=",y)
    if event==cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_LBUTTONDOWN):
        print("Mouse clicked and MOVED: X=",x,"Y=",y)
        global_x=x
        global_y=y
cv2.setMouseCallback('canvas',enable_draw)  
#cv2.resizeWindow('canvas',600,600)      
print("press: b for blue and r for red")
while True:
    cv2.imshow("canvas",canvas)
    #canvas[global_y][global_x]=color
    cv2.circle(canvas,(global_x,global_y),4,color,-1)
    ch=cv2.waitKey(1)
    if ch & 0xFF ==ord('b'):
        color=(255,0,0)
        
    elif ch & 0xFF ==ord('r'):
        color=(0,0,255)

    if ch & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()