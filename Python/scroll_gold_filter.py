import glob
import cv2
import numpy as np
import ntpath
from PIL import Image

path = "/home/pi/Documents/Graphene_Database/*.JPG"
for fname in glob.glob(path):
    frame = cv2.imread(fname)
    file_name = ntpath.basename(fname)
    print(file_name)
    # Convert BGR to HSV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([10,30,150])
    upper_blue = np.array([35,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(gray, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
##    frame = cv2.resize(frame,(600,380))
##    cv2.imshow('frame',frame)
##    mask = cv2.resize(mask,(600,380))
##    cv2.imshow('mask',mask)
##    res = cv2.resize(res,(600,380))
##    cv2.imshow('result',res)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
    vis = np.concatenate((frame, res), axis=1)
##    cv2.imshow('compare',vis)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
    cv2.imwrite("/home/pi/Documents/Graphene_Database/Filtered/filtered_%s" %file_name, vis)