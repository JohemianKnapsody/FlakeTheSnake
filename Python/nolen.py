import cv2
import numpy as np
import colorsys

image_corners = cv2.imread('/home/pi/Downloads/five_layer/17.jpg')
image_centre = cv2.imread('/home/pi/Downloads/five_layer/18.jpg')

centre_cropped = image_corners[0:480, 240:400]

image_0=image_centre
image_0[0:480, 240:400] = centre_cropped

image_1 = cv2.imread('/home/pi/Downloads/five_layer/16.jpg')
image_neutral= image_0

height, width = image_1.shape[:2]
image_neutral = image_1-image_0+128

cv2.imwrite("/home/pi/Pictures/equalised.jpeg", image_neutral)

hsv_image = cv2.cvtColor(image_neutral, cv2.COLOR_BGR2HSV)
height, width = image_neutral.shape[:2]
            
for x in range(0,width):
    for y in range(0,height):
        if image_neutral[y,x][0]<=140 and image_neutral[y,x][0]>=120 and image_neutral[y,x][1]<=135 and image_neutral[y,x][1]>=125 and image_neutral[y,x][2]<=124 and image_neutral[y,x][2]>=114 and hsv_image[y,x][0]<=100 and hsv_image[y,x][0]>=70 and hsv_image[y,x][1]<=31 and hsv_image[y,x][1]>=12 and hsv_image[y,x][2]<=133 and hsv_image[y,x][2]>=122:
            image_neutral[y,x]=[200, 200, 200]
        else:
            image_neutral[y,x]=[0, 0, 0]            

cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/home/pi/Pictures/detect.jpeg", image_neutral)

image_neutral = cv2.cvtColor(image_neutral,cv2.COLOR_BGR2GRAY)

thresh = 50
image_neutral = cv2.threshold(image_neutral, thresh, 220, cv2.THRESH_BINARY)[1]

##find contours of bulk flakes
contours = cv2.findContours(image_neutral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

##draw circles
for c in contours:
    #get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    #convert all valus to int
    center = (int(x), int(y))
    radius = int(radius)
    
    if 3 < radius:
        #and draw the cirlce in blue
        image_neutral = cv2.circle(image_neutral, center, radius, (255, 0, 0), 1)
        image_1 = cv2.circle(image_1, center, radius, (255, 0, 0), 1)
        print(center)
            
cv2.imshow('OG',image_neutral)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('OG',image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/home/pi/Pictures/detected.jpeg", image_1)