import cv2

# load the image
img = cv2.imread("/home/pi/Pictures/bored.jpeg")
# convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# resize for the visualization purposes
#img = cv2.resize(img, None, img, fx=0.4, fy=0.4)
# find edges with Canny
edges = cv2.Canny(img, 3000, 7000, apertureSize=7)
# show and save the result
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.imwrite("/home/pi/Pictures/bored_edges.jpeg", edges)
cv2.destroyAllWindows()