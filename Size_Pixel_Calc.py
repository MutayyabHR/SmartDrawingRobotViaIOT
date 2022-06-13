import skimage.measure
from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2
import picamera
import glob
import numpy as np
import time
import requests

res_w=648
res_h=486

camera= picamera.PiCamera()
camera.resolution = (res_w,res_h)
camera.iso=800
camera.shutter_speed=1000000
camera.capture('RefIMG1.jpg')
imageA = cv2.imread("RefIMG1.jpg", 1)

r=requests.get("http://192.168.100.40/forward")
time.sleep(5)
r=requests.get("http://192.168.100.40/forward")
time.sleep(5)

for i in range(10):
    print(i)
    time.sleep(1)

camera.capture('RefIMG2.jpg')
imageB = cv2.imread("RefIMG2.jpg", 1)

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

try:
    sorted_ = sorted(cnts,key=cv2.contourArea,reverse=True)
    biggest = sorted_[0]
    cv2.drawContours(frame,biggest,-1,(255,0,0),1)
    
except:
    pass

x1,y1,w1,h1=cv2.boundingRect(biggest)

#Physical Dimensions of Changes Area in Centimeters
W_original = 37
H_original = 13

for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

Pixel_Area=w1*h1
cm_area=W_original*H_original

print("Width in Pixels: ", w1)
print("Height in Pixels: ", h1)
print("Area in Pixels: ", Pixel_Area)

print("Width in Centimeters: ", W_original)
print("Height in Centimeters ", H_original)
print("Area in Centimeters: ", cm_area)

#Pixels Per Centimeter Ratio


Surface_Width=(W_original*res_w)/w1
Surface_Height=(H_original*res_h)/h1
Surface_Area=Surface_Width*Surface_Height

print("Surface Width in Meters: ", Surface_Width/100)
print("Surface Height in Meters: ", Surface_Height/100)
print("Area Of the Surface: ", Surface_Area)

#Taking The Robot to the starting point
url="http://192.168.100.40"

Dis_X = (W_original/w1)*x1+20
Dis_Y = (H_original/h1)*y1

i = int(Dis_X/10)
j = int(Dis_Y/10)
k = int((Dis_X%10)/2)
l = int((Dis_Y%10)/2)


for a in range(i):
    r=requests.get(url,"/back")
    if(r.text=="Back_Done"):
        time.sleep(5)

for b in range(k):
    r=requests.get(url,"/back")
    if(r.text=="Back_Done"):
        time.sleep(5)

r=requests.get(url,"/left")
if(r.text=="Left_Done"):
    time.sleep(5)
        
for a in range(j):
    r=requests.get(url,"/forward")
    if(r.text=="Forward_Done"):
        time.sleep(5)
        
for a in range(l):
    r=requests.get(url,"/Forward_2")
    if(r.text=="Forward_Done"):
        time.sleep(5)
        
r=requests.get(url,"/right")
if(r.text=="Right_Done"):
    time.sleep(5)

camera.close()

cv2.imwrite("Original.jpg",imageA)
cv2.imwrite("Modified.jpg",imageB)
cv2.imwrite("Diff.jpg",diff)
cv2.imwrite("Thresh.jpg",thresh)
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)