import cv2
import numpy as np
from matplotlib import pyplot as plt
import ntpath
import glob
import os

path = "/home/pi/Desktop/images/tiling/16/*.JPG"

length=len(glob.glob(path))
print(length)
array=[""]*length

topLeft=[[0,0] for i in range(length-1)]
overall_down=[0 for i in range(length)]
overall_right=[0 for i in range(length)]

across=4

result=np.zeros((960,1280,3), np.uint8)

for fname in glob.glob(path):
    frame = cv2.imread(fname)
    name=os.path.basename(fname)
    name=int(os.path.splitext(name)[0])
    print(name)
    
    array[name-1]=cv2.imread(fname)
    
##    cv2.imshow("cropped", array[name-1])
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()

(h, w) = array[0].shape[:2]
result[0:h,0:w]=array[0]

for n in range(0,length-1):
    
    (h, w) = array[n].shape[:2]
    (h1, w1) = array[n+1].shape[:2]
    if n>1 and (n+1)%across==0:
        overlap = array[n+1][0:45, 0:w1]
    else:
        overlap = array[n+1][0:h1, 0:85]

    if n>1 and (n+1)%across==0:
        res = cv2.matchTemplate(array[n-across+1], overlap, cv2.TM_CCOEFF)
    else:
        res = cv2.matchTemplate(array[n], overlap, cv2.TM_CCOEFF)
    (_, _, minLoc, maxLoc) = cv2.minMaxLoc(res)
    topLeft[n]= maxLoc
    
    if n>1 and (n+1)%across==0:
        overall_down[n+1]=overall_down[n-across+1]+topLeft[n][1]
        overall_right[n+1]=overall_right[n-across+1]+topLeft[n][0]
    else:
        overall_down[n+1]=overall_down[n]+topLeft[n][1]
        overall_right[n+1]=overall_right[n]+topLeft[n][0]
    
    result[overall_down[n+1]:overall_down[n+1]+h1,overall_right[n+1]:overall_right[n+1]+w1]=array[n+1]

cv2.imshow("cropped", result)
cv2.waitKey(0)
cv2.destroyAllWindows()