# import the necessary packages
import cv2
 
# load the image and show it
image = cv2.imread("/home/pi/Pictures/flake.jpeg")
cv2.imshow("original", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
print (image.shape)

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 200.0 / image.shape[1]
dim = (200, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
centre = (w / 2, h / 2)
 
# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(centre, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(centre)

cropped = image[263:h, 0:338]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("/home/pi/Pictures/flake_cropped.jpeg", cropped)