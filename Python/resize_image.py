import cv2

dst = cv2.imread("/home/pi/Pictures/background.jpeg")

cv2.imshow("it woks!",dst)

cv2.waitKey(500)

cv2.destroyAllWindows()

dst = cv2.resize(dst,(360,480))
dst = cv2.resize(dst,(36,48))

cv2.imshow("it woks?",dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
