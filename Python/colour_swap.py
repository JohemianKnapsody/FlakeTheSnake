import cv2
import numpy as np
import colorsys

image = cv2.imread('/home/pi/Downloads/TI180228/28183147.JPG')
new_height = 299
new_width = int(image.shape[1]*new_height/image.shape[0])
image = cv2.resize(image,(new_width,new_height))
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
height, width = image.shape[:2]

for x in range(0,width):
    for y in range(0,height):
        if hsv_image[y,x][0]<=9 and hsv_image[y,x][1]<=178 and hsv_image[y,x][2]<=133 and hsv_image[y,x][2]>=125:
            image[y,x]=[255,0,0]
            
cv2.imshow('OG',image)
cv2.waitKey(0)
cv2.destroyAllWindows()