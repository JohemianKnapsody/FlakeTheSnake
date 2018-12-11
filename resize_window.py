import cv2

img = cv2.imread('/home/pi/Downloads/Fused.jpg')
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
screen_res = 1280, 720

scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)

cv2.resizeWindow('Resized Window', 600, 1000)

cv2.imshow('Resized Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()