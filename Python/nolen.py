import cv2
import numpy as np
import colorsys

image_1 = cv2.imread('/home/pi/Downloads/16.jpg')
image_1_store = image_1
image_0 = cv2.imread('/home/pi/Downloads/background_1.jpg')
image_neutral= image_0

kernel = np.ones((3,3),np.float32)/9
image_1 = cv2.filter2D(image_1,-1,kernel)
image_0 = cv2.filter2D(image_0,-1,kernel)

##r = 600.0 / image_1.shape[1]
##dim = (600, int(image_1.shape[0] * r))
## 
### perform the actual resizing of the image and show it
##image_1 = cv2.resize(image_1, dim, interpolation = cv2.INTER_AREA)
##image_0 = cv2.resize(image_0, dim, interpolation = cv2.INTER_AREA)

height, width = image_1.shape[:2]
image_neutral = image_1-image_0+128

cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/home/pi/Pictures/equalised.jpeg", image_neutral)

hsv_image = cv2.cvtColor(image_neutral, cv2.COLOR_BGR2HSV)
height, width = image_neutral.shape[:2]
##
##image_greyscale = [[None]*height for _ in range(width)]

##for x in range(0,width):
##    for y in range(0,height):
##        if hsv_image[y,x][0]<=81 and hsv_image[y,x][0]>=79 and hsv_image[y,x][1]<=31 and hsv_image[y,x][1]>=15 and hsv_image[y,x][2]<=141 and hsv_image[y,x][2]>=132:
##            image_neutral[y,x]=[200, 200, 200]
##        else:
##            image_neutral[y,x]=[0, 0, 0]
            
for x in range(0,width):
    for y in range(0,height):
        if image_neutral[y,x][0]<=137 and image_neutral[y,x][0]>=128 and image_neutral[y,x][1]<=143 and image_neutral[y,x][1]>=133 and image_neutral[y,x][2]<=127 and image_neutral[y,x][2]>=118 and hsv_image[y,x][0]<=84 and hsv_image[y,x][0]>=77 and hsv_image[y,x][1]<=33 and hsv_image[y,x][1]>=13 and hsv_image[y,x][2]<=143 and hsv_image[y,x][2]>=130:
            image_neutral[y,x]=[200, 200, 200]
        else:
            image_neutral[y,x]=[0, 0, 0]
            
##for x in range(0,width):
##    for y in range(0,height):
##        if 0.3*int(image_neutral[y,x][2])+0.59*int(image_neutral[y,x][1])+0.11*int(image_neutral[y,x][0]) > 170:
##            image_neutral[y,x]=(192,192,192)
##        elif 0.3*int(image_neutral[y,x][2])+0.59*int(image_neutral[y,x][1])+0.11*int(image_neutral[y,x][0]) > 138:
##            image_neutral[y,x]=(100,100,100)
##        else:
##            image_neutral[y,x]=(0,0,0)
            

cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_neutral = cv2.cvtColor(image_neutral,cv2.COLOR_BGR2GRAY)

thresh = 100
image_neutral = cv2.threshold(image_neutral, thresh, 220, cv2.THRESH_BINARY)[1]

cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()

##find contours of bulk flakes
contours = cv2.findContours(image_neutral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

##draw circles
for c in contours:
    #get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    #convert all valus to int
    center = (int(x), int(y))
    radius = int(radius)
    
    if 1 < radius:
        #and draw the cirlce in blue
        image_neutral = cv2.circle(image_neutral, center, radius, (255, 0, 0), 2)
        print(center)
            
cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()