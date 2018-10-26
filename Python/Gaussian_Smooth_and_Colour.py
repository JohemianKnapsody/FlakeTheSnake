import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/pi/Downloads/TI180228/28183147.JPG')

new_height = 200
new_width = int(img.shape[1]*new_height/img.shape[0])
img = cv2.resize(img,(new_width,new_height))

kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)

dst = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

height, width = dst.shape[:2]

for x in range(0,width):
    for y in range(0,height):
        if dst[y,x][0]<=9 and dst[y,x][1]<=178 and dst[y,x][2]<=133 and dst[y,x][2]>=125:
            img[y,x]=[255, 255, 255]
            
##import image as greyscale
image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
           
cv2.imshow('OG',image_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

thresh = 254
image_grey = cv2.threshold(image_grey, thresh, 255, cv2.THRESH_BINARY)[1]
          
cv2.imshow('OG',image_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

##find contours of bulk flakes
contours = cv2.findContours(image_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

##draw circles
for c in contours:
    #get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    #convert all valus to int
    center = (int(x), int(y))
    radius = int(radius)
    
    if 3 < radius:
        #and draw the cirlce in blue
        img = cv2.circle(img, center, radius, (255, 0, 0), 1)
        
new_height = 500
new_width = int(img.shape[1]*new_height/img.shape[0])
img = cv2.resize(img,(new_width,new_height))
            
cv2.imshow('OG',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
