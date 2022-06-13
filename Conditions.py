import cv2
import glob
import numpy as np
import picamera

usr_in=input('Please Input Character: ')
usr_in=usr_in.upper();
print("Your input is : ", usr_in)

res_w=648
res_h=486

#camera = picamera.PiCamera()
#camera.resolution = (res_w,res_h)
#camera.iso=800
#camera.shutter_speed=1000000
#camera.capture('wboard.jpg')
img1 = cv2.imread("wboard.jpg", 1)
imgA=cv2.imread("A-01.jpg",1)
imgB=cv2.imread("B-01.jpg",1)
imgC=cv2.imread("C-01.jpg",1)
imgD=cv2.imread("D-01.jpg",1)
imgE=cv2.imread("E-01.jpg",1)
imgF=cv2.imread("F-01.jpg",1)
imgG=cv2.imread("G-01.jpg",1)
imgH=cv2.imread("H-01.jpg",1)
imgI=cv2.imread("I-01.jpg",1)
imgJ=cv2.imread("J-01.jpg",1)
imgK=cv2.imread("K-01.jpg",1)
imgL=cv2.imread("L-01.jpg",1)
imgM=cv2.imread("M-01.jpg",1)
imgN=cv2.imread("N-01.jpg",1)
imgO=cv2.imread("O-01.jpg",1)
imgP=cv2.imread("P-01.jpg",1)
imgQ=cv2.imread("Q-01.jpg",1)
imgR=cv2.imread("R-01.jpg",1)
imgS=cv2.imread("S-01.jpg",1)
imgT=cv2.imread("T-01.jpg",1)
imgU=cv2.imread("U-01.jpg",1)
imgV=cv2.imread("V-01.jpg",1)
imgW=cv2.imread("W-01.jpg",1)
imgX=cv2.imread("X-01.jpg",1)
imgY=cv2.imread("Y-01.jpg",1)
imgZ=cv2.imread("Z-01.jpg",1)

white=(255,255,255)
black=[0,0,0]
imgCrop=cv2.resize(img1, (res_w,res_h), interpolation=cv2.INTER_AREA)

if usr_in=='A':
    imgA=cv2.imread("A-01.jpg",1)
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgA[(i-1),(j-1),0]==0 and imgA[(i-1),(j-1),1]==0 and imgA[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    ##cv2.imshow('A',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)

elif usr_in=='B':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgB[(i-1),(j-1),0]==0 and imgB[(i-1),(j-1),1]==0 and imgB[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    ##cv2.imshow('B',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)

elif usr_in=='C':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgC[(i-1),(j-1),0]==0 and imgC[(i-1),(j-1),1]==0 and imgC[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('C',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='D':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgD[(i-1),(j-1),0]==0 and imgD[(i-1),(j-1),1]==0 and imgD[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('D',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='E':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgE[(i-1),(j-1),0]==0 and imgE[(i-1),(j-1),1]==0 and imgE[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('E',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='F':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgF[(i-1),(j-1),0]==0 and imgF[(i-1),(j-1),1]==0 and imgF[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('F',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='G':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgG[(i-1),(j-1),0]==0 and imgG[(i-1),(j-1),1]==0 and imgG[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('G',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='H':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgH[(i-1),(j-1),0]==0 and imgH[(i-1),(j-1),1]==0 and imgH[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('H',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='I':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgI[(i-1),(j-1),0]==0 and imgI[(i-1),(j-1),1]==0 and imgI[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('I',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)

elif usr_in=='J':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgJ[(i-1),(j-1),0]==0 and imgJ[(i-1),(j-1),1]==0 and imgJ[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('J',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='K':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgK[(i-1),(j-1),0]==0 and imgK[(i-1),(j-1),1]==0 and imgK[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('K',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)

elif usr_in=='L':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgL[(i-1),(j-1),0]==0 and imgL[(i-1),(j-1),1]==0 and imgL[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('J',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='M':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgM[(i-1),(j-1),0]==0 and imgM[(i-1),(j-1),1]==0 and imgM[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('M',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)

elif usr_in=='N':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgN[(i-1),(j-1),0]==0 and imgN[(i-1),(j-1),1]==0 and imgN[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('N',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='O':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgO[(i-1),(j-1),0]==0 and imgO[(i-1),(j-1),1]==0 and imgO[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('O',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='P':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgP[(i-1),(j-1),0]==0 and imgP[(i-1),(j-1),1]==0 and imgP[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('P',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='Q':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgQ[(i-1),(j-1),0]==0 and imgQ[(i-1),(j-1),1]==0 and imgQ[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('Q',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='R':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgR[(i-1),(j-1),0]==0 and imgR[(i-1),(j-1),1]==0 and imgR[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('R',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='S':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgS[(i-1),(j-1),0]==0 and imgS[(i-1),(j-1),1]==0 and imgS[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('S',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='T':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgT[(i-1),(j-1),0]==0 and imgT[(i-1),(j-1),1]==0 and imgT[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('T',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='U':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgU[(i-1),(j-1),0]==0 and imgU[(i-1),(j-1),1]==0 and imgU[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('U',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='V':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgV[(i-1),(j-1),0]==0 and imgV[(i-1),(j-1),1]==0 and imgV[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('V',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='W':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgW[(i-1),(j-1),0]==0 and imgW[(i-1),(j-1),1]==0 and imgW[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('W',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='X':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgX[(i-1),(j-1),0]==0 and imgX[(i-1),(j-1),1]==0 and imgX[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('X',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='Y':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgY[(i-1),(j-1),0]==0 and imgY[(i-1),(j-1),1]==0 and imgY[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('Y',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)
    
elif usr_in=='Z':
    for i in range(1,(res_h+1)):
         for j in range(1,(res_w+1)):
             if imgZ[(i-1),(j-1),0]==0 and imgZ[(i-1),(j-1),1]==0 and imgZ[(i-1),(j-1),2]==0:
                 imgCrop[(i-1),(j-1)]=black
    #cv2.imshow('Z',imgCrop)
    cv2.imwrite("1out.jpg",imgCrop)


#camera.close()