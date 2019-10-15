#!/usr/bin/env python
# coding: utf-8


import os
import webbrowser as web
import datetime
import cv2
path= 'E:/dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
count=1
while True:
    if count==2:
        break
    else:
        ret,im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
		
                cv2.putText(im,"Recognised -- Added to the list",(10,200),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0.233,9),2)
                with open("helloworld.txt", "a+") as filehandle:
                    filehandle.write('The presentees are with %d on %s.\n' % (Id,datetime.datetime.now()))
                count=count+1
                break
        else:
            cv2.putText(im,"No face found",(100,200),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0.233,9),2)
    
    cv2.imshow('im',im) 
    if cv2.waitKey(4000) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

