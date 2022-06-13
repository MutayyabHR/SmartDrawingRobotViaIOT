import numpy as np
import cv2
import picamera


res_w=648
res_h=486

camera= picamera.PiCamera()
camera.resolution = (res_w,res_h)
camera.iso=800
camera.shutter_speed=1000000
camera.capture('wboard.jpg')

image = cv2.imread("wboard.jpg", 1)
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized image", resized)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(image, (5,5), 0)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("blurred image", resized)
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", edged)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} boundaries in this image".format(len(cnts)))
boundary = resized.copy()
cv2.drawContours(boundary, cnts, -1, (0, 255, 0), 2)
cv2.imshow("boundary", boundary)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

print("REC #{}".format(i + 1))
detected_edge = resized[y:y + h, x:x + w]
cv2.imshow("Frame", boundary)

mask = np.zeros(resized.shape[:2], dtype="uint8")
((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
mask = mask[y:y + h, x:x + w]
final_image=cv2.bitwise_and(detected_edge, detected_edge, mask=mask)
cv2.imshow("Masked Frame ", final_image)

cv2.imwrite('final_img.jpg', final_image)

img1=cv2.imread('final_img.jpg',1)

cv2.imwrite("img2.jpg",img1)

camera.close()