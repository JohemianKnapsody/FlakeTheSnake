import cv2

img = cv2.imread('/home/pi/Downloads/Fused.jpg')
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)

##overestimate to allow movement and toolbars to be visible
screen_res = 1240, 680

print(img.shape)

scale_width = screen_res[0] / img.shape[0]
scale_height = screen_res[1] / img.shape[1]
scale = min(scale_width, scale_height)
print(scale)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.resizeWindow('Resized Window', window_width, window_height)

cv2.imshow('Resized Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()