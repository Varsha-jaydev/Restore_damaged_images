import cv2
import numpy as np

image = cv2.imread('damaged_image.jpg')

marked_damages = cv2.imread('mask_image.jpg', 0)

ret, thresh1 = cv2.threshold(marked_damages, 254, 255, cv2.THRESH_BINARY)


kernel = np.ones((7,7), np.uint8)
mask = cv2.dilate(thresh1, kernel, iterations = 1)

restored = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('damaged_image', image)
cv2.imshow('Restored', restored)
cv2.waitKey(0)
cv2.destroyAllWindows()