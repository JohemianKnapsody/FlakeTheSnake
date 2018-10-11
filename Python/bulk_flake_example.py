import cv2
import numpy as py

##import image as greyscale
image = cv2.imread("/home/pi/Pictures/flakes/flake_1.JPG",0)

##convert to binary 
im_bw = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#thresh = 130
#im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

##find contours of bulk flakes
contours = cv2.findContours(im_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

image2 = cv2.imread("/home/pi/Pictures/flakes/flake_1.JPG")

##draw circles
for c in contours:
    #get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    #convert all valus to int
    center = (int(x), int(y))
    radius = int(radius)
    
    if 20 < radius < 82 or radius > 86:
        #and draw the cirlce in blue
        image2 = cv2.circle(image2, center, radius, (255, 0, 0), 3)

#cv2.drawContours(image2, contours, -1, (255,0,0),3)

cv2.imshow("contoured binary image",image2)
cv2.waitKey(0)
