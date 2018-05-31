import os, sys 
import logging, time 
import numpy as np 
import cv2 
import cv2.cv as cv


face_cacade = 'haarcascade_frontalface_default.xml'

xml = cv2.CascadeClassifier(face_cascade)

# array_of_images = [] --> "abba.png"

#for image in array_of_images:         
img   = cv2.imread("abba.png")
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray  = cv2.equalizeHist(gray)
**r**  =  []
x  =  []
#cv2.CascadeClassifier.detectMultiScale(image, rejectLevels, levelWeights[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize[, outputRejectLevels]]]]]]) → objects
faces = xml.detectMultiScale(image = img, rejectLevels = **r**, levelWeights = x ,scaleFactor=1.05, minNeighbors=1, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
file_out  = open('faces_score.txt','w+',0)
for (x,y,w,h) in faces: 
       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
       roi_gray  = gray[y:y+h, x:x+w]
       roi_color = img[y:y+h, x:x+w]
       print **r**, x