import cv2
import Size_Pixel_Calc as PxSize
import Conditions
import glob
import requests
import time
import numpy as np
from requests.exceptions import HTTPError
import ImageCapture_Crop

res_w = 648
res_h = 486

S_Width=PxSize.Surface_Width
S_Height=PxSize.Surface_Height
Surface_Area=PxSize.Surface_Area

Sx=int((10*res_w)/S_Width)
Sy=int((2*res_h)/S_Height)

usr_in=Conditions.usr_in;
imgCrop=Conditions.imgCrop;

imgCrop = cv2.imread("1out.jpg",1)

RZ_img=cv2.resize(imgCrop, (Sx,Sy), interpolation=cv2.INTER_AREA)
cv2.imwrite("Z_Out_Img.jpg",RZ_img)

for i in range(Sy):
    for j in range(Sx):
        if(RZ_img[(i-1),(j-1),0]==0 and RZ_img[(i-1),(j-1),1]==0 and RZ_img[(i-1),(j-1),2]==0):
            r=requests.get(url,"/pendown")
            if(r.text=="PenDown_Done"):
                time.sleep(5)
        else:
            r=requests.get(url,"/penup")
            if(r.text=="PenUp_Done"):
                time.sleep(5)
        r=requests.get(url,"/forward")
        if(r.text=="Forward_Done"):
        time.sleep(5)
    if(Sy%2==0):
        r=requests.get(url,"/right")
        if(r.text=="Right_Done"):
        time.sleep(5)
        r=requests.get(url,"/Forward_2")
        if(r.text=="Forward_2_Done"):
        time.sleep(5)
        r=requests.get(url,"/right")
        if(r.text=="Right_Done"):
        time.sleep(5)
    else:
        r=requests.get(url,"/left")
        if(r.text=="Left_Done"):
        time.sleep(5)
        r=requests.get(url,"/Forward_2")
        if(r.text=="Forward_2_Done"):
        time.sleep(5)
        r=requests.get(url,"/left")
        if(r.text=="Left_Done"):
        time.sleep(5)