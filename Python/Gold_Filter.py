import cv2
import numpy as np

frame = cv2.imread('/home/pi/Downloads/flake_1.JPG')
# Convert BGR to HSV
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([10,30,150])
upper_blue = np.array([35,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(gray, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
frame = cv2.resize(frame,(600,380))
cv2.imshow('frame',frame)
mask = cv2.resize(mask,(600,380))
cv2.imshow('mask',mask)
res = cv2.resize(res,(600,380))
cv2.imshow('result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
