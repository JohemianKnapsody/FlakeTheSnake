import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('/home/pi/Downloads/32 (1).jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('/home/pi/Downloads/cross.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where( res >= threshold)
combined = []

for pt in zip(*loc[::-1]):
##    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    combined.append(pt[0]+pt[1])


top_left_index=(combined.index(min(combined)))
top_left= [loc[::-1][0][top_left_index],loc[::-1][1][top_left_index]]

cv2.rectangle(img_rgb, (top_left[0],top_left[1]), (top_left[0] + w, top_left[1] + h), (255,255,0),1)

print("0,0 coordinate at %s" %top_left)

cv2.imshow("cropped", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
##cv2.imwrite('/home/pi/Pictures/res.png',img_rgb)