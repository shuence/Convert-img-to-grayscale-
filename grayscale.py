import cv2

filename = 'Eye.jpeg'
img = cv2.imread(filename)
print(img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image',img)
cv2.imshow('Gray image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
