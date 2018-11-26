# import the necessary packages
import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

# load the image, clone it, and setup the mouse callback function
image = cv2.imread("/home/pi/Downloads/location/Fused2x2_scanned.jpg")
clone = image.copy()
cv2.namedWindow("image")
image_to_open = cv2.imread("/home/pi/Downloads/location/Fused2x2.jpg")
image_to_open_clone = image_to_open.copy()
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
		
	elif key == ord("q"):
		break

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		if len(refPt) == 2:
                    left = min(refPt[1][1],refPt[0][1])
                    top = max(refPt[1][0],refPt[0][0])
                    right = max(refPt[1][1],refPt[0][1])
                    base = min(refPt[1][0],refPt[0][0])
                    centre = (left+(right/2),(base+top/2))
                    roi = image_to_open_clone[left:right, base:top]
                    
                    cv2.imwrite("/home/pi/Pictures/%s_%s.jpeg" %(centre[1], centre[0]),roi)
                    cv2.imshow("ROI", roi)
                    cv2.waitKey(0)
                    cv2.destroyWindow("ROI")
                    cv2.waitKey(1)
                    
                    image = clone.copy()

cv2.destroyAllWindows()